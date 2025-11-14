import unittest
from main import foundLetterInWord

class TestFoundLetterInWord(unittest.TestCase):
    def test_common_cases(self):
        self.assertEqual(foundLetterInWord("banana", "a"), 3)
        self.assertEqual(foundLetterInWord("apple", "p"), 2)
        self.assertEqual(foundLetterInWord("hello", "x"), 0)
        self.assertEqual(foundLetterInWord("Mississippi", "s"), 4)
        self.assertEqual(foundLetterInWord("Test", "t"), 2)  

    def test_case_insensitive(self):
        self.assertEqual(foundLetterInWord("BaNaNa".lower(), "A".lower()), 3)

if __name__ == "__main__":
    unittest.main()
