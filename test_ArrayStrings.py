import unittest
from ArraysStrings import *

class TestArrayStrings(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique("helolol"), False)
        self.assertEqual(is_unique("helo"), True)
        self.assertEqual(is_unique("eelo"), False)
        self.assertEqual(is_unique("eloo"), False)

    def test_is_permutation(self):
        self.assertEqual(is_permutation('', ''), True)
        self.assertEqual(is_permutation('abc',  'cba'), True)
        self.assertEqual(is_permutation('abc',  'aba'), False)
        self.assertEqual(is_permutation('abc',  'cb'), False)

    def test_urlify(self):
        string = list("Mr John Smith    ")
        self.assertEqual(urlify(string), "Mr%20John%20Smith")

if __name__ == '__main__':
    unittest.main()


