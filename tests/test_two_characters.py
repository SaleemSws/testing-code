import unittest
from aie_code.two_characters import alternate


class TestTwoCharacters(unittest.TestCase):
    def test_empty_and_single(self):
        self.assertEqual(alternate(""), 0)
        self.assertEqual(alternate("a"), 0)

    def test_two_characters(self):
        self.assertEqual(alternate("ab"), 2)
        self.assertEqual(alternate("aa"), 0)
        self.assertEqual(alternate("abab"), 4)

    def test_three_characters(self):
        self.assertEqual(alternate("abc"), 2)
        self.assertEqual(alternate("aba"), 3)
        self.assertEqual(alternate("bab"), 3)

    def test_no_valid_pattern(self):
        self.assertEqual(alternate("aaa"), 0)
        self.assertEqual(alternate("aabb"), 0)
        self.assertEqual(alternate("abcabc"), 4)

    def test_complex_patterns(self):
        self.assertEqual(alternate("beabeefeab"), 5)  # 'babab'
        self.assertEqual(alternate("asdcbsdcagfsdbgdfanfghbsfdab"), 8)  # 'bsbsbsbs'
        self.assertEqual(alternate("asvkugfiugsalddlasguifgukvsa"), 0)

    def test_repeated_patterns(self):
        self.assertEqual(alternate("abababab"), 8)
        self.assertEqual(alternate("cdcdcdcd"), 8)
        self.assertEqual(alternate("abcabcabc"), 6)

    def test_mixed_cases(self):
        self.assertEqual(alternate("ABab"), 2)
        self.assertEqual(alternate("abAB"), 2)
        self.assertEqual(alternate("AaBbA"), 3)

    def test_special_cases(self):
        # Test with spaces and special characters
        self.assertEqual(alternate("a b a b"), 4)
        self.assertEqual(alternate("a!b!a!b"), 4)
        self.assertEqual(alternate("a1b1a1b"), 4)

    def test_long_strings(self):
        self.assertEqual(alternate("ab" * 100), 200)
        self.assertEqual(alternate("abc" * 100), 200)
        self.assertEqual(alternate("a" * 100), 0)

    def test_edge_cases(self):
        # Test with adjacent duplicates
        self.assertEqual(alternate("aabbcc"), 0)
        # Test with single character repeating
        self.assertEqual(alternate("aaabbb"), 0)
        # Test with mixed valid and invalid patterns
        self.assertEqual(alternate("abaacdcd"), 4)
