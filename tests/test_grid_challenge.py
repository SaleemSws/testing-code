import unittest
from aie_code.grid_challenge import gridChallenge


class TestGridChallenge(unittest.TestCase):
    def test_empty_grid(self):
        self.assertEqual(gridChallenge([]), "NO")

    def test_single_element(self):
        self.assertEqual(gridChallenge(["a"]), "YES")
        self.assertEqual(gridChallenge(["z"]), "YES")

    def test_single_row(self):
        self.assertEqual(gridChallenge(["abc"]), "YES")
        self.assertEqual(gridChallenge(["cba"]), "YES")
        self.assertEqual(gridChallenge(["zzz"]), "YES")

    def test_single_column(self):
        self.assertEqual(gridChallenge(["a", "b", "c"]), "YES")
        self.assertEqual(gridChallenge(["z", "y", "x"]), "NO")
        self.assertEqual(gridChallenge(["a", "a", "a"]), "YES")

    def test_2x2_grid(self):
        self.assertEqual(gridChallenge(["ab", "cd"]), "YES")
        self.assertEqual(gridChallenge(["ba", "dc"]), "YES")
        self.assertEqual(gridChallenge(["zz", "aa"]), "NO")

    def test_3x3_grid(self):
        self.assertEqual(gridChallenge(["abc", "def", "ghi"]), "YES")
        self.assertEqual(gridChallenge(["cba", "fed", "ihg"]), "YES")
        self.assertEqual(gridChallenge(["abc", "hgf", "def"]), "NO")

    def test_equal_characters(self):
        self.assertEqual(gridChallenge(["aaa", "aaa", "aaa"]), "YES")
        self.assertEqual(gridChallenge(["zzz", "zzz", "zzz"]), "YES")

    def test_mixed_cases(self):
        self.assertEqual(
            gridChallenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(gridChallenge(["abc", "lmp", "qrt"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")

    def test_edge_cases(self):
        # Test with maximum characters
        self.assertEqual(gridChallenge(["zyx", "wvu", "tsr"]), "NO")

        # Test with mixed order
        self.assertEqual(gridChallenge(["abc", "bcd", "cde"]), "YES")
        self.assertEqual(gridChallenge(["abc", "bcd", "ced"]), "YES")

        # Test boundary cases
        self.assertEqual(gridChallenge(["z", "a"]), "NO")
        self.assertEqual(gridChallenge(["a", "z"]), "YES")

    def test_larger_grids(self):
        large_valid = ["abcde", "fghij", "klmno", "pqrst", "uvwxy"]
        self.assertEqual(gridChallenge(large_valid), "YES")

        large_invalid = [
            "abcde",
            "fghij",
            "klmno",
            "pqrsz",
            "uvwyx",
        ]
        self.assertEqual(gridChallenge(large_invalid), "NO")
