#!/usr/bin/env python3

import string
import random


def random_chars(length):
    for i in range(length):
        yield random.choice(string.ascii_letters)

random_string = ''.join(list(random_chars(1000)))
print(random_string)
