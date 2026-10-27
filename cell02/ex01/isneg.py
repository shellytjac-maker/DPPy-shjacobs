#! /usr/bin/env python3

number = int(input("Enter a number: "))
if number < 0:
    print("This number is negative.")
elif number == 0:
    print("This number is both negtive and positive.")
else:
    print("This number is positive.")