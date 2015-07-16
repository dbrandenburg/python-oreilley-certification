#!/usr/bin/env python3

import re

def anonymize():
    string = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
    pattern="(\d{4}-){3}"
    repl="XXXX-XXXX-XXXX-"
    return re.sub(pattern, repl, string)

#"a function that substitutes X for all but the last four digits of any credit card numbers in a string" means any string, not just the specific example string.
#So whereas it's fine to pass the example string as an argument and in fact the project requests that you do so, anonymize should not hard-wire itself to any particular string.
#Also, if the string contains "1234-AAAA" that should not trigger a replacement.  Include some tests where you try to fool it. 
#Only the pattern XXXX-XXXX-XXXX-XXXX -- and no others  -- should trigger substitution.
#Good work so far.

#-Kirby