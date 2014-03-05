from morse_translator.translator import Translator, TranslationException


class App():
    """
    Class to encapsulate console interface
    """
    def __init__(self):
        self.input_str = ""
        self.translated_str = ""

    def greet_user(self):
        """
        Output a little ascii graphic to the console
        """
        print ""
        print "============================"
        print "    MORSE CODE CONVERTER    "
        print "============================"
        print ""

    def prompt_for_input(self):
        """
        Take input from the user to hand off to the translator
        """
        print "Please input a string you'd like converted into morse."
        print "Valid characters include a-z, A-Z, 0-9, and \" \""
        print ""

        self.input_str = raw_input("input: ")

    def translate_input_to_morse(self):
        """
        Hand off input to translator.
        If translator throws an error, output error message to console then exit.
        """
        print "\n-----\n"
        print "You entered: \"%s\"" % self.input_str

        translator = Translator()
        try:
            upper_str = self.input_str.upper()
            self.translated_str = translator.to_morse(upper_str)
        except TranslationException as e:
            print "Error: %s" % e.msg
            print "\tIn input: %s" % e.expr
            print "\tAt character: %s" % e.entry
            print ""
            print "Please try again with a valid input."
            print "Valid characters include a-z, A-Z, 0-9, and \" \""
            exit(0)  # end execution

    def output_translation(self):
        """
        Show user the translated text
        """
        print "Translation: %s" % self.translated_str


def run():
    app = App()
    app.greet_user()
    app.prompt_for_input()
    app.translate_input_to_morse()
    app.output_translation()

if __name__ == "__main__":
    run()