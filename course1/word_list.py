#!/usr/local/bin/python3

user_text = str(input("Input your text:"))
words = user_text.split(" ")
uppercase_contained_list = []
lowercase_all_list = []

for word in words:
    contains_upper = False
    for letter in word:
        if letter == letter.upper():
            contains_upper = True
            break
    if contains_upper == True:
        uppercase_contained_list.append(word)
    else:
        lowercase_all_list.append(word)

for word in (uppercase_contained_list+lowercase_all_list):
    print(word)
    
    