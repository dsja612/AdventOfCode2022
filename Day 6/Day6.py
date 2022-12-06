input = open("Day 6/input.txt", "r")

data = input.readlines()[0]
data_list = [char for char in data]

for i in range(len(data)):
    if len(data_list[i:i+4]) == len(set(data_list[i:i+4])): # Set removes duplicates
        print("Part one: {}".format(i + 4))
        break

for i in range(len(data)):
    if len(data_list[i:i+14]) == len(set(data_list[i:i+14])):
        print("Part two: {}".format(i + 14))
        break