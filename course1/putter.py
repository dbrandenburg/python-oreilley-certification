#!/usr/local/bin/python3

while True:
    atextfile = open('textfile.txt','a')
    rtextfile = open('textfile.txt','r')
    
    print(rtextfile.readline())
    rtextfile.close()
    
    userinput = str(input("Enter text:"))
    if not userinput:
        break
    atextfile.write(userinput)
    atextfile.close()