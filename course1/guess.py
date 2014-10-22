#!/usr/local/bin/python3
"""This program guesses a number. 5 tries allowed."""

secret = 12

def start_guess(secret,min_number,max_number):
    
    tries = 0
    guess  = 0
    
    while guess != secret:
        tries +=1
        guess = int(input("Guess a number:"))
        if tries >= 5:
            print("Sorry, the number was", secret)
            break
        elif guess < min_number or guess > max_number:
            print("please choose a value between 1 and ",max_number)
            continue
        elif guess < secret:
            print("Guess higher")
        elif guess > secret:
    	    print("Guess lower")
        else:
    	    print("Correct! Well done, the number was", secret)
    	    