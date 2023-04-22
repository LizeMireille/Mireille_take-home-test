import unittest
from isbn_final import check_isbn

class Test_ISBN(unittest.TestCase):
    def test_valid_isbn13(self):
        isbn_num = "9780316066525"
        self.assertEqual(check_isbn(isbn_num), "Valid")

    def test_invalid_isbn13(self):
        isbn_num = "9783876155237"
        self.assertEqual(check_isbn(isbn_num), "Invalid")

    def test_valid_isbn10_X(self):
        isbn_num = "817450494X"
        self.assertEqual(check_isbn(isbn_num), "Valid")

    def test_invalid_isbn10_X(self):
        isbn_num = "030640615X"
        self.assertEqual(check_isbn(isbn_num), "Invalid")

    def test_valid_isbn10(self):
        isbn_num = "0679722769"
        self.assertEqual(check_isbn(isbn_num), "Valid")

    def test_invalid_isbn10(self):
        isbn_num = "0345453747"
        self.assertEqual(check_isbn(isbn_num), "Invalid")

    def test_invalid_short(self):
        isbn_num = "12345"
        self.assertEqual(check_isbn(isbn_num), "Invalid")
    
    def test_invalid_long(self):
        isbn_num = "123456789012345678"
        self.assertEqual(check_isbn(isbn_num), "Invalid")
    
    def test_invalid_char(self):
        isbn_num = "abcf24w4tgfu7"
        self.assertEqual(check_isbn(isbn_num), "Invalid")

if __name__ == '__main__':
    unittest.main()
