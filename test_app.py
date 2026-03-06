"""Unit tests for words.py (non-GUI logic)."""

import unittest
from words import random_label, ADJECTIVES, NOUNS


class TestRandomLabel(unittest.TestCase):
    """Test the random_label helper."""

    def test_returns_string(self):
        label = random_label()
        self.assertIsInstance(label, str)

    def test_has_two_words(self):
        label = random_label()
        parts = label.split()
        self.assertEqual(len(parts), 2)

    def test_words_from_vocabulary(self):
        for _ in range(50):
            adj, noun = random_label().split()
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == "__main__":
    unittest.main()
