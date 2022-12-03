import os
from queue import PriorityQueue

path = "C:\\Users\\dsja6\\OneDrive - National University of Singapore\\Projects\\AdventOfCode2022\\Day 1"
os.chdir(path)

input = open("input.txt", "r")

pq = PriorityQueue()
cur = 0

for line in input:
    if line != "\n":
        cur += int(line)
    else:
        # Invert priority
        pq.put(cur * -1, cur)
        cur = 0

# Part 1
print(pq.queue[0] * -1)

# Part 2
sum = 0
for i in range(3):
    sum += pq.get() * -1
print(sum)