class Dictionary():
    """
    Class to encapsulate mapping of A-Z, 0-9 to their corresponding morse value.

    Morse code expresses characters as pulses of different durations.
    Short signals are referred to as "dots", long signals as "dashes".

    We'll refer to "dots" as the character "." and "dashes" as "_"
    Example:  "A" translates to "dot", "dash" in morse.
              In our dictionary, we'll store the key "A" with value ". _"

    Dictionary transcribed from international morse code
    Referenced from http://en.wikipedia.org/wiki/File:International_Morse_Code.svg
    """
    def __init__(self):
        self.dictionary = {
            "A": ". -",
            "B": "_ . . .",
            "C": "_ . _ .",
            "D": "_ . .",
            "E": ".",
            "F": ". . _ .",
            "G": "_ _ .",
            "H": ". . . .",
            "I": ". .",
            "J": ". _ _ _",
            "K": "_ . _",
            "L": ". _ _ _",
            "M": "_ _",
            "N": "_ .",
            "O": "_ _ _",
            "P": ". _ _ .",
            "Q": "_ _ . _",
            "R": ". _ .",
            "S": ". . .",
            "T": "_",
            "U": ". . _",
            "V": ". . . _",
            "W": ". _ _",
            "X": "_ . . _",
            "Y": "_ . _ _",
            "Z": "_ _ . .",
            "0": "_ _ _ _ _",
            "1": ". _ _ _ _",
            "2": ". . _ _ _",
            "3": ". . . _ _",
            "4": ". . . . _",
            "5": ". . . . .",
            "6": "_ . . . .",
            "7": "_ _ . . .",
            "8": "_ _ _ . .",
            "9": "_ _ _ _ .",
            " ": " "            # Space will map to itself
        }

    def find(self, key):
        """
        Performs a lookup of key in morse dictionary.
        If key exists, return corresponding value.
        If key does not exist, return None.
        """
        return self.dictionary.get(key) # will return None if key doesn't exist