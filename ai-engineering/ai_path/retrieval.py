"""P02: independent BM25 teaching baseline with server-supplied tenant scope."""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import date
import json
import math
from pathlib import Path
import re
from time import perf_counter

DATA = Path(__file__).resolve().parents[1] / "data"


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str
    tenant: str
    valid_until: str | None = None


def load_documents(path: Path = DATA / "documents.json") -> list[Document]:
    docs = [Document(**row) for row in json.loads(path.read_text())]
    if len({doc.id for doc in docs}) != len(docs):
        raise ValueError("duplicate document id")
    for doc in docs:
        if doc.valid_until:
            date.fromisoformat(doc.valid_until)
    return docs


class SearchIndex:
    def __init__(self, documents: list[Document]):
        self.documents = documents

    def search(self, query: str, tenant: str, k: int = 3, *, as_of: str | None = None,
               method: str = "bm25") -> list[dict]:
        if type(k) is not int or not 1 <= k <= 10:
            raise ValueError("k must be an integer in [1, 10]")
        if not isinstance(query, str) or not query.strip() or len(query) > 500:
            raise ValueError("query must contain 1 to 500 characters")
        if method not in {"overlap", "bm25"}:
            raise ValueError("unknown retrieval method")
        today = date.fromisoformat(as_of) if as_of else date.today()
        # Filter before scoring: inaccessible content must not influence ranking.
        eligible = [doc for doc in self.documents
                    if doc.tenant in {"public", tenant}
                    and (doc.valid_until is None or date.fromisoformat(doc.valid_until) >= today)]
        terms = [Counter(tokenize(doc.title + " " + doc.text)) for doc in eligible]
        if not eligible:
            return []
        lengths = [sum(counter.values()) for counter in terms]
        avg_length = sum(lengths) / len(lengths) or 1.0
        query_terms = set(tokenize(query))
        df = Counter(term for counter in terms for term in counter)
        scored = []
        for doc, counter, length in zip(eligible, terms, lengths):
            score = 0.0
            for term in query_terms:
                tf = counter[term]
                if not tf:
                    continue
                if method == "overlap":
                    score += 1
                else:
                    idf = math.log(1 + (len(eligible) - df[term] + 0.5) / (df[term] + 0.5))
                    score += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * length / avg_length))
            if score > 0:
                scored.append({"id": doc.id, "title": doc.title, "text": doc.text,
                               "score": score})
        return sorted(scored, key=lambda row: (-row["score"], row["id"]))[:k]


def evaluate(index: SearchIndex, cases: list[dict], k=3, method="bm25") -> dict:
    if not cases:
        raise ValueError("evaluation set cannot be empty")
    recalls, reciprocals, details, timings, abstentions = [], [], [], [], []
    for case in cases:
        start = perf_counter()
        hits = index.search(case["query"], case["tenant"], k, as_of=case["as_of"], method=method)
        timings.append((perf_counter() - start) * 1000)
        ids = [row["id"] for row in hits]
        gold = set(case["relevant_ids"])
        if gold:
            recalls.append(len(gold & set(ids)) / len(gold))
            reciprocals.append(next((1 / (i + 1) for i, doc in enumerate(ids) if doc in gold), 0))
        else:
            abstentions.append(int(not hits))
        details.append({"case_id": case["id"], "slice": case["slice"], "retrieved": ids,
                        "relevant": sorted(gold)})
    return {"method": method, "k": k, "cases": len(cases),
            "answerable_cases": len(recalls), "unanswerable_cases": len(abstentions),
            "recall_at_k": sum(recalls) / len(recalls) if recalls else None,
            "mrr_at_k": sum(reciprocals) / len(reciprocals) if reciprocals else None,
            "empty_result_rate_on_unanswerable": sum(abstentions) / len(abstentions) if abstentions else None,
            "mean_latency_ms": sum(timings) / len(timings), "details": details}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("outputs/p02.json"))
    args = parser.parse_args()
    cases = json.loads((DATA / "queries.json").read_text())
    index = SearchIndex(load_documents())
    result = {"project": "P02", "measurement_origin": "local_cpu_measured",
              "scope": "retrieval only, original synthetic English SDK documents",
              "generation_evaluated": False,
              "results": [evaluate(index, cases, method=m) for m in ("overlap", "bm25")]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
