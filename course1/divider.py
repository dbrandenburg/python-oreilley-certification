#!/usr/local/bin/python3

print("Dividing 10 by an integer")
while True:
    try:
        divisor = int(input("Provide an integer: "))
        print(10 / divisor)
    except(ValueError):
        print("Your input must be an integer")
    except(ZeroDivisionError):
        print("Your input must not be zero (0)")