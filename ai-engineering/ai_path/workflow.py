"""P03: durable, approval-gated simulated reservation workflow, without an LLM."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3


class WorkflowStore:
    def __init__(self, path: str | Path):
        self.path = str(path)
        if self.path == ":memory:":
            raise ValueError("use a file so independent transactions share durable state")
        with self.connect() as con:
            con.executescript("""
                CREATE TABLE IF NOT EXISTS inventory(sku TEXT PRIMARY KEY, quantity INTEGER NOT NULL CHECK(quantity>=0));
                CREATE TABLE IF NOT EXISTS tasks(id TEXT PRIMARY KEY, tenant TEXT NOT NULL, sku TEXT NOT NULL,
                    quantity INTEGER NOT NULL CHECK(quantity>0), status TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, task_id TEXT NOT NULL, event TEXT NOT NULL);
                INSERT OR IGNORE INTO inventory VALUES('SIM-KIT', 10);
            """)

    @contextmanager
    def connect(self):
        con = sqlite3.connect(self.path, timeout=5)
        con.row_factory = sqlite3.Row
        try:
            with con:
                yield con
        finally:
            con.close()

    def propose(self, task_id: str, tenant: str, sku: str, quantity: int) -> dict:
        if not task_id or not tenant or sku != "SIM-KIT" or type(quantity) is not int or quantity <= 0:
            raise ValueError("invalid reservation request")
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            row = con.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
            if row:
                if (row["tenant"], row["sku"], row["quantity"]) != (tenant, sku, quantity):
                    raise ValueError("idempotency key reused for a different request")
                return dict(row)
            con.execute("INSERT INTO tasks VALUES(?,?,?,?,?)",
                        (task_id, tenant, sku, quantity, "WAITING_APPROVAL"))
            con.execute("INSERT INTO events(task_id,event) VALUES(?,?)", (task_id, "PROPOSED"))
        return self.get(task_id, tenant)

    def get(self, task_id: str, tenant: str) -> dict:
        with self.connect() as con:
            row = con.execute("SELECT * FROM tasks WHERE id=? AND tenant=?", (task_id, tenant)).fetchone()
            if row is None:
                raise KeyError("task not found")
            return dict(row)

    def approve(self, task_id: str, tenant: str, *, actor_role: str) -> dict:
        if actor_role != "reviewer":
            raise PermissionError("reviewer role required")
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            row = con.execute("SELECT * FROM tasks WHERE id=? AND tenant=?", (task_id, tenant)).fetchone()
            if row is None:
                raise KeyError("task not found")
            if row["status"] == "WAITING_APPROVAL":
                con.execute("UPDATE tasks SET status='APPROVED' WHERE id=?", (task_id,))
                con.execute("INSERT INTO events(task_id,event) VALUES(?,?)", (task_id, "APPROVED"))
        return self.get(task_id, tenant)

    def execute(self, task_id: str, tenant: str, *, fail_before_commit=False) -> dict:
        with self.connect() as con:
            con.execute("BEGIN IMMEDIATE")
            row = con.execute("SELECT * FROM tasks WHERE id=? AND tenant=?", (task_id, tenant)).fetchone()
            if row is None:
                raise KeyError("task not found")
            if row["status"] == "SUCCEEDED":
                return dict(row)
            if row["status"] != "APPROVED":
                raise PermissionError("task has not been approved")
            changed = con.execute("UPDATE inventory SET quantity=quantity-? WHERE sku=? AND quantity>=?",
                                  (row["quantity"], row["sku"], row["quantity"])).rowcount
            if not changed:
                raise ValueError("insufficient inventory")
            con.execute("UPDATE tasks SET status='SUCCEEDED' WHERE id=?", (task_id,))
            con.execute("INSERT INTO events(task_id,event) VALUES(?,?)", (task_id, "SUCCEEDED"))
            if fail_before_commit:
                raise RuntimeError("injected failure before transaction commit")
        return self.get(task_id, tenant)

    def inventory(self) -> int:
        with self.connect() as con:
            return int(con.execute("SELECT quantity FROM inventory WHERE sku='SIM-KIT'").fetchone()[0])

    def events(self, task_id: str, tenant: str) -> list[str]:
        self.get(task_id, tenant)
        with self.connect() as con:
            return [row[0] for row in con.execute("SELECT event FROM events WHERE task_id=? ORDER BY id", (task_id,))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--database", type=Path, default=Path("outputs/workflow.sqlite"))
    args = parser.parse_args()
    args.database.parent.mkdir(parents=True, exist_ok=True)
    store = WorkflowStore(args.database)
    store.propose("demo-001", "demo", "SIM-KIT", 2)
    # Simulated reviewer input. A deployed service must derive roles from identity.
    store.approve("demo-001", "demo", actor_role="reviewer")
    first = store.execute("demo-001", "demo")
    second = store.execute("demo-001", "demo")
    print(json.dumps({"task": first, "retry_same_result": first == second,
                      "inventory": store.inventory(), "events": store.events("demo-001", "demo"),
                      "scope": "local simulated reservation; deterministic controller; no LLM or external writes"}))


if __name__ == "__main__":
    main()
