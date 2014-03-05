# Morse Code Translator
---

This is one of the first toys I made when I first started learning python.
It's seen a number of revisions since then, but the basic idea remains the same.

Input a string of characters and gets back a sequence that spells it out in morse code.
Accepted characters are "a-z", "A-Z", "0-9", and " ".

Then throw an error if any invalid characters are encountered.
Error message should include which character was invalid.

To run the app:

    python app.py

To run tests:

    python tests/test_all.py
    python test/test_*.py

Improvements to make in the future:

* Add sound capability
* It'd be pretty sweet to have it actually play out the dots and dashes when it outputs
* Maybe an actual GUI using Tkinter?
* I'm still undecided to that end. I haven't seen a lot of uses with Tkinter.

