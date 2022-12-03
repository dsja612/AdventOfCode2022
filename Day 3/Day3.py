input = open("Day 3/input.txt", "r")

item = {}
priority = 0

# Part one
for line in input:
    length = len(str(line))

    # first half
    for i in range(0, int(length/2)):
        if line[i] not in item:
            item[line[i]] = 1

    # second half
    for i in range(int(length/2), length):
        if line[i] in item:
            if line[i].islower():
                priority += ord(line[i]) - ord('a') + 1
            else:
                priority += ord(line[i]) - ord('A') + 27
            item.clear()
            break
    
print("Part one: {}".format(priority))

# Part two
input = open("Day 3/input.txt", "r") #new file descriptor
counter = 1
priority = 0

for line in input:
    for i in range(0, len(str(line))):
        # Add each char to dict once per iteration
        if counter % 3 == 1:
            if line[i] not in item:
                item[line[i]] = 1
        elif counter % 3 == 2:
            if line[i] in item:
                item[line[i]] = 2
        else:
            if line[i] in item:
                # Prevent keyerror
                if item[line[i]] == 2:
                    if line[i].islower():
                        priority += ord(line[i]) - ord('a') + 1
                    else:
                        priority += ord(line[i]) - ord('A') + 27
                    item.clear()
                    break
    counter += 1

print("Part two: {}".format(priority))