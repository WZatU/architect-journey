"""Behavioral and leakage checks. Run: python -m unittest discover -s tests -v."""

import unittest

import numpy as np

from recommender import (Event, FEATURE_NAMES, Ranker, TOPICS, auc, evaluate, features,
                         log_loss_from_logits, make_data, popularity, recall, recommend,
                         training_examples, user_profile)


class RecommendationTests(unittest.TestCase):
    def setUp(self):
        self.videos, self.events = make_data(seed=7, n_users=8, n_videos=60, steps=30)

    def test_seed_reproduces_exposures_and_labels(self):
        self.assertEqual((self.videos, self.events),
                         make_data(seed=7, n_users=8, n_videos=60, steps=30))

    def test_current_and_future_labels_do_not_change_current_features(self):
        x, y, users = training_examples(self.videos, self.events)
        altered = self.events.copy()
        index = 24
        old = altered[index]
        altered[index] = Event(old.timestamp, old.user_id, old.video_id,
                               1.0 if old.watch_ratio < 0.8 else 0.0, not old.liked)
        x2, y2, _ = training_examples(self.videos, altered)
        np.testing.assert_array_equal(x[:index + 1], x2[:index + 1])
        self.assertFalse(np.array_equal(y[index], y2[index]))
        later = np.flatnonzero(users[index + 1:] == old.user_id)[0] + index + 1
        self.assertFalse(np.array_equal(x[later], x2[later]))

    def test_order_is_chronological_and_duplicate_timestamps_rejected(self):
        original = training_examples(self.videos, self.events)
        reversed_result = training_examples(self.videos, list(reversed(self.events)))
        for a, b in zip(original, reversed_result):
            np.testing.assert_array_equal(a, b)
        with self.assertRaises(ValueError):
            training_examples(self.videos, [self.events[0], self.events[0]])

    def test_skips_and_likes_change_interest_in_opposite_directions(self):
        cold = user_profile([], self.videos)
        like = user_profile([Event(0, 0, 0, 1.0, True)], self.videos)
        skip = user_profile([Event(0, 0, 0, 0.01, False)], self.videos)
        self.assertGreater(like[0], cold[0])
        self.assertLess(skip[0], cold[0])
        self.assertAlmostEqual(float(like.sum()), 1.0)
        self.assertTrue(np.all(skip > 0))

    def test_recall_excludes_seen_and_has_no_duplicates(self):
        history = [e for e in self.events if e.user_id == 0]
        popular = popularity(self.videos, self.events[:120])
        candidates = recall(history, self.videos, popular, np.random.default_rng(42))
        self.assertEqual(len(candidates), len(set(candidates)))
        self.assertFalse(set(candidates) & {e.video_id for e in history})

    def test_recommend_cold_start_exploration_and_exhausted_catalog(self):
        model = Ranker(np.zeros((len(FEATURE_NAMES), 2)))
        popular = popularity(self.videos, [])
        rows = recommend(model, self.videos, [], popular, k=10, exploration=0.2)
        self.assertEqual(len(rows), 10)
        self.assertEqual(len({r["video_id"] for r in rows}), 10)
        self.assertEqual(sum(r["exploration"] for r in rows), 2)
        self.assertTrue(all(np.isfinite(r["score"]) for r in rows))
        history = [Event(i, 0, i, 0.5, False) for i in range(len(self.videos))]
        self.assertEqual(recommend(model, self.videos, history, popular), [])
        self.assertEqual(recommend(model, self.videos, [], popular, k=0), [])

    def test_topic_penalty_changes_an_otherwise_tied_feed(self):
        model = Ranker(np.zeros((len(FEATURE_NAMES), 2)))
        rows = recommend(model, self.videos, [], popularity(self.videos, []),
                         k=6, exploration=0, diversity_penalty=0.12)
        self.assertEqual(len({r["topic"] for r in rows}), len(TOPICS))

    def test_gradient_training_learns_a_separable_problem(self):
        rng = np.random.default_rng(4)
        x = np.column_stack((np.ones(500), rng.normal(size=500)))
        y = np.column_stack((x[:, 1] > 0, x[:, 1] < 0)).astype(float)
        model, training = Ranker.fit(x[:400], y[:400], x[400:], y[400:], epochs=150)
        self.assertLess(log_loss_from_logits(y[400:], x[400:] @ model.weights), 0.3)
        self.assertGreater(auc(y[400:, 0], model.predict(x[400:])[:, 0]), 0.98)
        self.assertGreater(training["best_epoch"], 0)

    def test_auc_ties_and_missing_class(self):
        self.assertEqual(auc([0, 1], [0.5, 0.5]), 0.5)
        self.assertEqual(auc([0, 1], [0, 1]), 1.0)
        self.assertEqual(auc([0, 1], [1, 0]), 0.0)
        self.assertIsNone(auc([1, 1], [0, 1]))

    def test_ndcg_known_order_and_no_positive_labels(self):
        y = np.array([[1, 1], [0, 0], [1, 0]], dtype=float)
        probabilities = np.array([[0.9, 0.9], [0.1, 0.1], [0.8, 0.1]])
        result = evaluate(y, probabilities, np.zeros(3))
        self.assertAlmostEqual(result["logged_ndcg@10"], 1.0)
        self.assertEqual(evaluate(np.zeros((3, 2)), probabilities, np.zeros(3))["logged_ndcg@10"], 0)

    def test_invalid_feedback_and_feature_shape(self):
        for ratio in (-0.1, 1.1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                Event(0, 0, 0, ratio, False)
        self.assertEqual(features(user_profile([], self.videos), self.videos[0]).shape,
                         (len(FEATURE_NAMES),))


if __name__ == "__main__":
    unittest.main()
