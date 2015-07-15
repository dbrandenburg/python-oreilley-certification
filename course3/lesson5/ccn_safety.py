#!/usr/bin/env python3

import re

def anonymize():
    string = "Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."
    pattern="\d{4}-"
    repl="XXXX-"
    return re.sub(pattern, repl, string)