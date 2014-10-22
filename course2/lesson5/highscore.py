#!/usr/bin/env python3
import shelve

def highscore(playername,score,db="highscore"):
    """Sets the highscore of a user in returns the highest score"""

    input_playername = str(playername)
    input_score = int(score)

    try:
        shelf = shelve.open(db)
    except IOError:
        print("IOError. Could not open shelve file.")
    
    try:
        score = shelf[input_playername]
    except KeyError:
        score = input_score
        shelf[input_playername] = score

    if input_score > score:
        shelf[input_playername] = input_score
        score = input_score
    
    shelf.close()
    return(score)
    
if __name__ == "__main__":
    score = highscore("Dennis",4,"local.shlf")
    print(score)