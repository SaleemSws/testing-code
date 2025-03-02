import unittest
from aie_code.caesar_cipher import caesarCipher


class TestCaesarCipher(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(caesarCipher("", 3), "")

    def test_lowercase_only(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")
        self.assertEqual(caesarCipher("xyz", 2), "zab")
        self.assertEqual(caesarCipher("abcxyz", 3), "defabc")

    def test_uppercase_only(self):
        self.assertEqual(caesarCipher("ABC", 1), "BCD")
        self.assertEqual(caesarCipher("XYZ", 2), "ZAB")
        self.assertEqual(caesarCipher("ABCXYZ", 3), "DEFABC")

    def test_non_alphabet_characters(self):
        self.assertEqual(caesarCipher("123", 5), "123")
        self.assertEqual(caesarCipher("!@#", 5), "!@#")
        self.assertEqual(caesarCipher("   ", 5), "   ")

    def test_mixed_content(self):
        self.assertEqual(caesarCipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(caesarCipher("abc123XYZ", 2), "cde123ZAB")
        self.assertEqual(caesarCipher("1a2b3c!", 4), "1e2f3g!")

    def test_large_rotation(self):
        self.assertEqual(caesarCipher("abc", 27), "bcd")  # 27 % 26 = 1
        self.assertEqual(caesarCipher("xyz", 28), "zab")  # 28 % 26 = 2
        self.assertEqual(caesarCipher("ABC", 52), "ABC")  # 52 % 26 = 0

    def test_zero_rotation(self):
        self.assertEqual(caesarCipher("Hello", 0), "Hello")
        self.assertEqual(caesarCipher("123!@#", 0), "123!@#")

    def test_full_alphabet(self):
        self.assertEqual(
            caesarCipher("abcdefghijklmnopqrstuvwxyz", 1), "bcdefghijklmnopqrstuvwxyza"
        )
        self.assertEqual(
            caesarCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25), "ZABCDEFGHIJKLMNOPQRSTUVWXY"
        )

    def test_negative_rotation(self):
        self.assertEqual(caesarCipher("abc", -1), "zab")
        self.assertEqual(caesarCipher("XYZ", -2), "VWX")
