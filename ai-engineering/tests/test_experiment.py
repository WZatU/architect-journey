import unittest

import numpy as np

from ai_path.experiment import grouped_split, make_telemetry, run_experiment


class ExperimentTests(unittest.TestCase):
    def test_device_partitions_are_disjoint_and_cover_rows(self):
        rows = make_telemetry()
        groups = np.asarray([row['device'] for row in rows])
        parts = grouped_split(groups)
        self.assertEqual(sorted(np.concatenate(parts).tolist()), list(range(len(rows))))
        for i in range(3):
            for j in range(i):
                self.assertFalse(set(groups[parts[i]]) & set(groups[parts[j]]))

    def test_seed_reproduces_data(self):
        self.assertEqual(make_telemetry(17), make_telemetry(17))
        self.assertNotEqual(make_telemetry(17), make_telemetry(18))

    def test_complete_experiment_has_holdout_metrics_and_baseline(self):
        report = run_experiment()
        self.assertEqual(sum(x['rows'] for x in report['split'].values()), 720)
        self.assertGreater(report['test']['macro_f1'], report['test']['baseline_macro_f1'])
        low, high = report['test']['device_bootstrap_accuracy_ci95']
        self.assertLessEqual(low, high)
        self.assertEqual(len(report['validation_trials']), 3)
        self.assertEqual(report['selected_C'], max(report['validation_trials'], key=lambda x:x['validation_macro_f1'])['C'])


if __name__ == '__main__':
    unittest.main()
