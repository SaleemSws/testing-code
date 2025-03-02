from coe_number.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_53_55_69(self):
        prime_list = [53, 55, 69]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)  # 55 and 69 are not prime

    def test_give_single_prime_number_is_prime(self):
        prime_list = [7]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_large_prime_numbers_is_prime(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_list_with_negative_number_is_not_prime(self):
        prime_list = [-2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)  # -2 is not prime
        # ตรงนี้จะ failed เพราะ -2 ไม่ใช่จำนวนเฉพาะ ต้องไปแก้ใน number_utils.py ให้เขียนเงื่อนไขเช็คว่าเลขติดลบหรือไม่ เพื่อแก้ failed test case นี้

    def test_give_list_with_composite_number_is_not_prime(self):
        prime_list = [2, 3, 9]  # 9 is composite (3x3)
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
