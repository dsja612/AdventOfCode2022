import os

path = "C:\\Users\\dsja6\\OneDrive - National University of Singapore\\Projects\\AdventOfCode2022\\Day 2"
os.chdir(path)

input = open("input.txt", "r")
score1 = 0
score2 = 0

map1 = {"A": {"X": 4, "Y": 8, "Z": 3},  # rock
        "B": {"X": 1, "Y": 5, "Z": 9},  # paper
        "C": {"X": 7, "Y": 2, "Z": 6}}  # scissors

map2 = {"A": {"X": 3, "Y": 4, "Z": 8},  # rock
        "B": {"X": 1, "Y": 5, "Z": 9},  # paper
        "C": {"X": 2, "Y": 6, "Z": 7}}  # scissors


for line in input:
    score1 += map1[line[0]][line[2]]
    score2 += map2[line[0]][line[2]]

print(score1)
print(score2)
