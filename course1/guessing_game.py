#!/usr/local/bin/python3
import random
import guess
min_number=1
max_number=99

secret = random.randint(min_number,max_number)
guess.start_guess(secret,min_number,max_number)
