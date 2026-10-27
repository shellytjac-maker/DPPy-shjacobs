#!/usr/bin/env python3

first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
result = first_number * second_number
if result < 0:
    print("The result is negative")
elif result == 0:
    print("The result is positive and negative")
else:
    print("The result is positive")