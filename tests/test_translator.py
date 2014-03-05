import unittest
from morse_translator.translator import Translator, TranslationException
from morse_translator.dictionary import Dictionary


class TranslatorTests(unittest.TestCase):

    def setUp(self):
        self.translator = Translator()

    def test_constructor(self):
        """
        Ensure the constructor returns non-null object of type Translator.
        And its property, dictionary, is non-null and of type Dictionary.
        """
        self.assertIsNotNone(self.translator)
        self.assertIsInstance(self.translator, Translator)
        self.assertIsNotNone(self.translator.dictionary)
        self.assertIsInstance(self.translator.dictionary, Dictionary)

    def test_to_morse_with_valid_input(self):
        """
        Ensure to_morse is evaluating correctly with valid inputs.
        Fail if an error is raised.
        """
        well_formed_input = "Hello world"
        expected_result = ". . . .  .  . _ _ _  . _ _ _  _ _ _     . _ _  _ _ _  . _ .  . _ _ _  _ . ."
        with self.assertRaises(TranslationException):
            result = self.translator.to_morse(well_formed_input)
            self.assertEquals(expected_result, result)

    def test_to_morse_with_invalid_input(self):
        """
        Ensure to_morse throws an error with invalid inputs.
        Fail if no error was raised.
        """
        invalid_input = "H! th#r3"
        with self.assertRaises(TranslationException):
            self.translator.to_morse(invalid_input)

    def test_exception_attributes(self):
        """
        Ensure our error handling is functioning as intended.
        It should contain the first character that execution failed with.
        """
        invalid_input = "H! th#r3"
        with self.assertRaises(TranslationException) as e:
            self.translator.to_morse(invalid_input)

        exception = e.exception
        self.assertEquals(exception.expr, invalid_input)
        self.assertEquals(exception.entry, invalid_input[1])
        self.assertEquals(exception.msg, "Key not found.")


def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
