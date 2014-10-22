#!/usr/local/bin/python3

message = str(input("Message: "))
secret = ""

for character in reversed(message):
    secret = secret + str(chr(ord(character)+1))
print(secret)