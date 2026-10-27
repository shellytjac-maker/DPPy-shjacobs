#!/usr/bin/env python3

numeric = int(input("Enter a number: "))
i = 0;
while i < 10:
    print(f"{i} * {numeric} = {i * numeric}")
    i += 1
    if i == 10:
        break
