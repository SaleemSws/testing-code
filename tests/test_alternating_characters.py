import unittest
from aie_code.alternating_characters import alternatingCharacters


class TestAlternatingCharacters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)
        self.assertEqual(alternatingCharacters("B"), 0)

    def test_no_deletions_needed(self):
        self.assertEqual(alternatingCharacters("AB"), 0)
        self.assertEqual(alternatingCharacters("BA"), 0)
        self.assertEqual(alternatingCharacters("ABAB"), 0)
        self.assertEqual(alternatingCharacters("BABA"), 0)

    def test_all_same_characters(self):
        self.assertEqual(alternatingCharacters("AAA"), 2)
        self.assertEqual(alternatingCharacters("BBBB"), 3)
        self.assertEqual(alternatingCharacters("AAAAA"), 4)

    def test_mixed_patterns(self):
        self.assertEqual(alternatingCharacters("AAAB"), 2)
        self.assertEqual(alternatingCharacters("ABAA"), 1)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)
        self.assertEqual(alternatingCharacters("ABBABB"), 2)

    def test_alternating_with_segments(self):
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAA"), 1)
        self.assertEqual(alternatingCharacters("BABAAABA"), 2)

    def test_long_strings(self):
        self.assertEqual(alternatingCharacters("A" * 100), 99)
        self.assertEqual(alternatingCharacters("AB" * 50), 0)
        self.assertEqual(alternatingCharacters("AAABBAABBB"), 6)
