#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for countdown in range(10, 0, -1):
        print(countdown)
    print("Happy New Year!")
    pass

def square_integers(int_list):
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def fizzbuzz(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string
