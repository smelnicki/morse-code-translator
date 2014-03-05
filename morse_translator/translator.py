class TranslationException(Exception):
    """
    Exception raised for errors during translation.

    Attributes:
        expr -- input expression in which the error occurred
        entry -- key which could not be found
        msg  -- explanation of the error
    """
    def __init__(self, expr, entry, msg):
        self.expr = expr
        self.entry = entry
        self.msg = msg


from dictionary import Dictionary


class Translator():
    """ Class to encapsulate morse translation logic. """
    def __init__(self):
        self.dictionary = Dictionary()

    def to_morse(self, input_str):
        """
        Evaluates each character of the input string by looking it up in the morse dictionary
        If the char exists in the dictionary, append its corresponding morse code value to a character list.
        If the char does not exist, raise a TranslationException.

        Returns the morse code character list joined together into a string, separated by spaces.
        """
        char_list = []
        for letter in input_str:
            entry = self.dictionary.find(letter)
            if entry:
                char_list.append(entry)
            else:
                raise TranslationException(input_str, letter, "Key not found.")

        return "  ".join(char_list)

