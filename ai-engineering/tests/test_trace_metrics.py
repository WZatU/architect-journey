import copy
import unittest

from ai_path.trace_metrics import summarize


class TraceTests(unittest.TestCase):
    def setUp(self):
        self.row = {'measurement_origin':'fixture','start_s':0.,'end_s':1.,
                    'token_times_s':[0.4,0.5,0.6],'output_tokens':3}

    def test_ttft_and_tpot_have_different_denominators(self):
        result = summarize([self.row])
        self.assertAlmostEqual(result['mean_ttft_s'], 0.4)
        self.assertAlmostEqual(result['mean_tpot_s'], 0.1)
        self.assertAlmostEqual(result['output_tokens_per_wall_second'], 3.)

    def test_single_token_tpot_is_undefined(self):
        row = dict(self.row, token_times_s=[0.4], output_tokens=1)
        self.assertIsNone(summarize([row])['mean_tpot_s'])

    def test_reject_nonfinite_unordered_and_count_mismatch(self):
        for update in [{'token_times_s':[0.5,0.4,0.6]}, {'end_s':float('nan')},
                       {'output_tokens':10}, {'measurement_origin':None}]:
            row = copy.deepcopy(self.row)
            row.update(update)
            with self.assertRaises(ValueError):
                summarize([row])

    def test_boolean_token_count_is_not_a_measurement(self):
        with self.assertRaises(ValueError):
            summarize([dict(self.row, token_times_s=[0.4], output_tokens=True)])

    def test_reject_mixed_measurement_origins(self):
        with self.assertRaises(ValueError):
            summarize([self.row, dict(self.row, measurement_origin='measured')])


if __name__ == '__main__':
    unittest.main()
