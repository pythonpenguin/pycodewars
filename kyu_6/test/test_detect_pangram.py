import unittest
import detect_pangram

class MyTestCase(unittest.TestCase):
    def test_pangram(self):
        self.assertEqual(detect_pangram.is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
    def test_not_pangram(self):
        self.assertEqual(detect_pangram.is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)


if __name__ == '__main__':
    unittest.main()
