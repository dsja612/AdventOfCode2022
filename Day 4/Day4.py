input = open("Day 4/input.txt", "r")

counter_one = 0
counter_two = 0

def check_one(x1: int, x2: int, y1: int, y2: int) -> bool:
    return ((x1 <= x2) and (y1 >= y2)) or ((x2 <= x1) and (y2 >= y1))

def check_two(x1: int, x2: int, y1: int, y2: int) -> bool:
    return (x1 <= y2) and (x2 <= y1)

for line in input:
    line = line.split(',')
    line1 = line[0].split('-')
    line2 = line[1].split('-')
    # Representation of ranges: x1 - y1, x2 - y2
    if check_one(int(line1[0]), int(line2[0]), int(line1[1]), int(line2[1])):
        counter_one += 1
    if check_two(int(line1[0]), int(line2[0]), int(line1[1]), int(line2[1])):
        counter_two += 1

print("Part one: {}".format(counter_one))
print("Part two: {}".format(counter_two))