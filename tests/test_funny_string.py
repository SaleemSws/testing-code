import unittest
from aie_code.funny_string import funnyString


class TestFunnyString(unittest.TestCase):
    def test_funny_string_cases(self):
        # กรณีที่เป็น Funny String (ค่าต่างของ ASCII ทั้งไปและกลับเท่ากัน)
        self.assertEqual(
            funnyString("abc"), "Funny"
        )  # |a-b|=1, |b-c|=1 เท่ากับ |c-b|=1, |b-a|=1
        self.assertEqual(funnyString("lmnop"), "Funny")  # ค่าต่าง ASCII เท่ากันทั้งไปและกลับ
        self.assertEqual(funnyString("abcba"), "Funny")  # palindrome จะเป็น Funny เสมอ

    def test_not_funny_string_cases(self):
        # กรณีที่ไม่เป็น Funny String (ค่าต่างของ ASCII ไปและกลับไม่เท่ากัน)
        self.assertEqual(
            funnyString("acb"), "Not Funny"
        )  # |a-c|=2, |c-b|=1 ไม่เท่ากับ |b-c|=1, |c-a|=2
        self.assertEqual(funnyString("adb"), "Not Funny")
        self.assertEqual(funnyString("wxa"), "Not Funny")

    def test_edge_cases(self):
        # ทดสอบกรณีพิเศษ
        self.assertEqual(funnyString("a"), "Funny")  # string ความยาว 1 ถือว่าเป็น Funny
        self.assertEqual(
            funnyString("aa"), "Funny"
        )  # string ที่ตัวอักษรเหมือนกันทั้งหมดเป็น Funny
        self.assertEqual(funnyString("aaa"), "Funny")  # ค่าต่าง ASCII = 0 ทั้งไปและกลับ

    def test_case_sensitivity(self):
        # ทดสอบความแตกต่างของตัวพิมพ์เล็ก/ใหญ่
        self.assertEqual(funnyString("aZaZ"), "Funny")  # ค่าต่าง ASCII เท่ากันทั้งไปและกลับ
        self.assertEqual(funnyString("AzA"), "Funny")  # palindrome กรณีผสมตัวพิมพ์
        self.assertEqual(funnyString("AbC"), "Not Funny")  # ค่าต่าง ASCII ไม่เท่ากัน

    def test_special_patterns(self):
        # ทดสอบรูปแบบพิเศษ
        self.assertEqual(funnyString("xyyx"), "Funny")  # mirror pattern
        self.assertEqual(funnyString("abccba"), "Funny")  # palindrome ยาว
        self.assertEqual(funnyString("abcdeg"), "Not Funny")  # เรียงลำดับปกติ
        self.assertEqual(funnyString("zabcd"), "Not Funny")  # เริ่มด้วย z
