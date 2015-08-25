#!/usr/bin/env python3
import random
from datetime import datetime, timedelta

def random_summands():
    a = random.randint(1,10)
    b = random.randint(1,10)
    return a,b

def user_input(summand, second_summand):
    input_text = "What is the sum of {0} and {1}?".format(summand, second_summand)
    summ = input(input_text)
    return summ

def check_result(summ,a,b):
    if int(summ) == a + b:
        return "right"
    else:
        return "wrong"


def run_test(number_of_questions):
    question = 1
    question_results = []
    total_time = 0

    while question <= number_of_questions:
        a,b = random_summands()
        start_time = datetime.now()
        summ = user_input(a, b)
        stop_time = datetime.now()
        time_taken = stop_time - start_time
        total_time += time_taken.seconds
        question += 1
        result = check_result(summ,a,b)
        print(summ + " is " + result + "!")
        question_results.append([question,time_taken.seconds,result])
    for item in question_results:
        print("Question {0} took about {1} seconds to complete and was {2}.".format(item[0], item[1], item[2]))
    print("You took {0} seconds to finish the quiz".format(total_time))
    print("Your average time was {0} seconds per question".format(total_time / (question - 1)))

if __name__ == "__main__":
    run_test(5)
