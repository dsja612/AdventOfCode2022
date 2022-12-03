import os
path = "C:\\Users\\dsja6\\OneDrive - National University of Singapore\\Projects\\AdventOfCode2022\\Day 1"
os.chdir(path)

input = open("input.txt", "r")

max = 0
cur = 0

for line in input:
    if line != "\n":
        cur += int(line)
    else:
        if cur > max:
            max = cur
        cur = 0

print(max)