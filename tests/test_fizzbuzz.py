import unittest
from aie_code.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_normal_numbers(self):
        self.assertEqual(
            fizzbuzz([1, 2, 4, 7, 8, 11, 13, 14]),
            ["1", "2", "4", "7", "8", "11", "13", "14"],
        )

    def test_fizz_numbers(self):
        self.assertEqual(fizzbuzz([3, 6, 9, 12]), ["Fizz", "Fizz", "Fizz", "Fizz"])

    def test_buzz_numbers(self):
        self.assertEqual(fizzbuzz([5, 10, 20, 25]), ["Buzz", "Buzz", "Buzz", "Buzz"])

    def test_fizzbuzz_numbers(self):
        self.assertEqual(
            fizzbuzz([15, 30, 45, 60]), ["FizzBuzz", "FizzBuzz", "FizzBuzz", "FizzBuzz"]
        )

    def test_mixed_sequence(self):
        self.assertEqual(
            fizzbuzz([1, 2, 3, 4, 5, 15]), ["1", "2", "Fizz", "4", "Buzz", "FizzBuzz"]
        )

    def test_empty_list(self):
        self.assertEqual(fizzbuzz([]), [])

    def test_negative_numbers(self):
        self.assertEqual(fizzbuzz([-3, -5, -15]), ["Fizz", "Buzz", "FizzBuzz"])

    def test_zero(self):
        self.assertEqual(fizzbuzz([0]), ["FizzBuzz"])

    def test_large_numbers(self):
        self.assertEqual(fizzbuzz([99, 100, 101]), ["Fizz", "Buzz", "101"])

    def test_consecutive_special_numbers(self):
        self.assertEqual(
            fizzbuzz([15, 16, 17, 18, 19, 20]),
            ["FizzBuzz", "16", "17", "Fizz", "19", "Buzz"],
        )

    def test_non_integer_handling(self):
        with self.assertRaises(TypeError):
            fizzbuzz([1, 2, "3"])
        with self.assertRaises(TypeError):
            fizzbuzz([1, 2.5, 3])

    def test_none_handling(self):
        with self.assertRaises(TypeError):
            fizzbuzz(None)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            fizzbuzz("123")
