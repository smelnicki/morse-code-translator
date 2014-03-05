import unittest
import string
from morse_translator.dictionary import Dictionary


class DictionaryTests(unittest.TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

    def test_constructor(self):
        """
        Ensure the constructor returns non-null object of type Dictionary.
        And its property, dictionary, is non-null and of type dict.
        """
        self.assertIsNotNone(self.dictionary)
        self.assertIsInstance(self.dictionary, Dictionary)
        self.assertIsNotNone(self.dictionary.dictionary)
        self.assertIsInstance(self.dictionary.dictionary, dict)

    def test_find(self):
        """
        Ensure find is returning non-null values for valid chars.
        Similarly, ensure that is is returning null for invalid chars.
        """
        alphabet = string.uppercase[:26]
        for letter in alphabet: # A-Z
            self.assertIsNotNone(self.dictionary.find(letter))

        numbers = range(10)
        for number in numbers:  # 0-9
            self.assertIsNotNone(self.dictionary.find(str(number)))

        invalid_chars = "!@#$%^&*()_+|?><,.:{}~"
        for char in invalid_chars:
            self.assertIsNone(self.dictionary.find(char))


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
