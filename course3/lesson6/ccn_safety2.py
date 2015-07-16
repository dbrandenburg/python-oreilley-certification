#!/usr/bin/env python3

import re

def anonymize():
    string = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
    pattern=re.compile(r"""
        (\d{4}-)    #First four digits of a credit card
        {3}         #Each set repeated 3 times
        """, re.VERBOSE)
    repl="XXXX-XXXX-XXXX-"
    return pattern.sub(repl, string)