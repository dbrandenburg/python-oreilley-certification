#!/usr/local/bin/python3

my_set = set()
my_dict = {}

while True:
    words=str(input("Enter text:"))
    if words == "": 
        print("Finished")
        break
        
    for word in words.strip().split():
        my_set_prelen=len(my_set)
        my_set.add(word)
        my_set_postlen=len(my_set)
        if my_set_prelen < my_set_postlen:
            my_dict.update({word: len(my_set)})
            
    for word in my_dict:
        print(word, ":", my_dict[word])
        
    