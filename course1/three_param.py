#!/usr/local/bin/python3

def my_func(a,b='b was not entered',c='c was not entered'):
    for param in [a,b,c]:
        print(param)
    
my_func('test')
my_func('test','test')
my_func('test','test','test')
print(my_func)