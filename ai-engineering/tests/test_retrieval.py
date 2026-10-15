import json
import unittest

from ai_path.retrieval import DATA, SearchIndex, evaluate, load_documents


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.index = SearchIndex(load_documents())

    def test_relevant_result_and_no_expired_document(self):
        hits = self.index.search('current firmware release', 'demo', as_of='2026-10-15')
        self.assertEqual(hits[0]['id'], 'sdk-current')
        self.assertNotIn('sdk-obsolete', [row['id'] for row in hits])

    def test_cross_tenant_content_never_returned(self):
        hits = self.index.search('CAL-OTHER-99 calibration identifier', 'demo', k=10)
        self.assertNotIn('other-private', [row['id'] for row in hits])
        self.assertTrue(any(row['id'] == 'other-private' for row in self.index.search('CAL-OTHER-99', 'other')))

    def test_invalid_requests(self):
        for query, k in [('', 3), ('a', 0), ('a', True), ('a' * 501, 3), (None, 3)]:
            with self.assertRaises(ValueError):
                self.index.search(query, 'demo', k)

    def test_metric_denominators_and_no_match(self):
        cases = [
            {'id':'a','query':'sim_start','tenant':'demo','as_of':'2026-10-15','relevant_ids':['sdk-start'],'slice':'lookup'},
            {'id':'b','query':'zz_no_match_zz','tenant':'demo','as_of':'2026-10-15','relevant_ids':[],'slice':'unanswerable'},
        ]
        result = evaluate(self.index, cases)
        self.assertEqual(result['answerable_cases'], 1)
        self.assertEqual(result['recall_at_k'], 1)
        self.assertEqual(result['empty_result_rate_on_unanswerable'], 1)

    def test_fixture_label_references_are_valid(self):
        ids = {doc.id for doc in self.index.documents}
        cases = json.loads((DATA / 'queries.json').read_text())
        self.assertEqual(len({case['id'] for case in cases}), len(cases))
        for case in cases:
            self.assertLessEqual(set(case['relevant_ids']), ids)


if __name__ == '__main__':
    unittest.main()
