#!/usr/local/bin/python3
"""Detect any mention of Python in the user's input."""
uin = input("Please enter: ")
if "python" in uin.lower():
    print("Pythooooon.")
elif "perl" in uin.lower():
    print("Arrrg, perl.")
else:
    print("Nope.")
