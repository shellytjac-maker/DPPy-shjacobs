#!/usr/bin/env python3

age = input("Please tell me your age: ")
print(f"You are currently {age} years old")
i = 10
while i <= 30:
    print(f"In {i} years, you'll be {int(age) + i}!")
    i += 10