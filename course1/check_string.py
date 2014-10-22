inputstring = input("Please enter an upper-case string ending with a period:")

if inputstring == inputstring.upper() and inputstring.endswith("."):
    print("Input meets both requirements.")
    
else:
    if inputstring != inputstring.upper():
        print("Input is not all upper case.")
        
    if not inputstring.endswith("."):
        print("Input does not end with a period.")
    

    