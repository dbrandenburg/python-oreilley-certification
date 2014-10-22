#!/usr/local/bin/python3
import sys

caser_options = {
    'capitalize': str.capitalize,
    'title': str.title,
    'upper': str.upper,
    'lower': str.lower,
    'exit': quit
}

options = caser_options.keys()

while True:
    option_prompt = 'Enter a function name ({0}): '.format(', '.join(options))
    string_prompt = 'Enter a string: '
    option_inp = str(input(option_prompt))
    option = caser_options.get(option_inp, None)
    
    if option_inp not in options:
        print("Option not in options list. Please choose one of the following: {0}".format(', '.join(options)))
        continue  
    string_inp = str(input(string_prompt))
    if option_inp == "exit":
        option("Goodbye for now!")
    print(option(string_inp))
   