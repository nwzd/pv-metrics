# Task 6: Part of unit tests
import unittest
from udfs import is_null_or_empty, is_not_null_nor_empty, trim_and_lower_case

class TestUDFs(unittest.TestCase):

    def test_is_null_or_empty(self):
        self.assertTrue(is_null_or_empty(None))
        self.assertTrue(is_null_or_empty(""))
        self.assertTrue(is_null_or_empty("   "))
        self.assertFalse(is_null_or_empty("test"))
        self.assertFalse(is_null_or_empty("  test  "))

    def test_is_not_null_nor_empty(self):
        self.assertFalse(is_not_null_nor_empty(None))
        self.assertFalse(is_not_null_nor_empty(""))
        self.assertFalse(is_not_null_nor_empty("   "))
        self.assertTrue(is_not_null_nor_empty("test"))
        self.assertTrue(is_not_null_nor_empty("  test  "))

    def test_trim_and_lower_case(self):
        self.assertEqual(trim_and_lower_case("  TEST  "), "test")
        self.assertEqual(trim_and_lower_case("  test  "), "test")
        self.assertEqual(trim_and_lower_case("TeSt"), "test")
        self.assertEqual(trim_and_lower_case("  TeSt  "), "test")
        self.assertEqual(trim_and_lower_case(""), "")
        self.assertEqual(trim_and_lower_case("   "), "")

if __name__ == '__main__':
    unittest.main()