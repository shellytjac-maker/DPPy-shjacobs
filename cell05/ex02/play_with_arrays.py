#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
newarray = []
for x in array:
    if x > 5:
        newarray.append(x + 2)

newSet = set(newarray)

print(array)
print(newarray)