from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import tempfile
import unittest

from ai_path.workflow import WorkflowStore


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / 'state.sqlite'
        self.store = WorkflowStore(self.path)
        self.store.propose('task-1', 'demo', 'SIM-KIT', 2)

    def tearDown(self):
        self.tmp.cleanup()

    def test_approval_required_and_tenant_scope(self):
        with self.assertRaises(PermissionError):
            self.store.execute('task-1', 'demo')
        with self.assertRaises(PermissionError):
            self.store.approve('task-1', 'demo', actor_role='reader')
        with self.assertRaises(KeyError):
            self.store.approve('task-1', 'other', actor_role='reviewer')
        self.assertEqual(self.store.inventory(), 10)

    def test_idempotency_key_cannot_change_payload(self):
        with self.assertRaises(ValueError):
            self.store.propose('task-1', 'demo', 'SIM-KIT', 3)

    def test_recovery_after_failure_before_commit(self):
        self.store.approve('task-1', 'demo', actor_role='reviewer')
        with self.assertRaises(RuntimeError):
            self.store.execute('task-1', 'demo', fail_before_commit=True)
        resumed = WorkflowStore(self.path)
        self.assertEqual(resumed.inventory(), 10)
        self.assertEqual(resumed.get('task-1', 'demo')['status'], 'APPROVED')
        resumed.execute('task-1', 'demo')
        self.assertEqual(resumed.inventory(), 8)

    def test_concurrent_duplicate_execution_has_one_effect(self):
        self.store.approve('task-1', 'demo', actor_role='reviewer')
        with ThreadPoolExecutor(max_workers=4) as pool:
            results = list(pool.map(lambda _: self.store.execute('task-1', 'demo'), range(8)))
        self.assertTrue(all(row['status'] == 'SUCCEEDED' for row in results))
        self.assertEqual(self.store.inventory(), 8)
        self.assertEqual(self.store.events('task-1', 'demo').count('SUCCEEDED'), 1)

    def test_insufficient_inventory_does_not_partially_commit(self):
        self.store.propose('big', 'demo', 'SIM-KIT', 100)
        self.store.approve('big', 'demo', actor_role='reviewer')
        with self.assertRaises(ValueError):
            self.store.execute('big', 'demo')
        self.assertEqual(self.store.inventory(), 10)
        self.assertEqual(self.store.get('big', 'demo')['status'], 'APPROVED')


if __name__ == '__main__':
    unittest.main()
