input = open("Day 5/input.txt", "r")

stacks = []
new_stacks = []
new_stacks_two = []

# Creating a list of stacks
stacks.append('BPNQHDRT')
stacks.append('WGBJTV')
stacks.append('NRHDSVMQ')
stacks.append('PZNMC')
stacks.append('DZB')
stacks.append('VCWZ')
stacks.append('GZNCVQLS')
stacks.append('LGJMDNV')
stacks.append('TPMFZCG')

# Initializing stacks from string
for stack in stacks:
    new_stacks.append([letter for letter in stack])
    new_stacks_two.append([letter for letter in stack])

# Part one
for line in input:
    instr = line.split(" ")
    for i in range(int(instr[1])):
        new_stacks[int(instr[5]) - 1].append(new_stacks[int(instr[3]) - 1].pop())

print("Part one: ", end = "")
for stack in new_stacks:
    print(stack.pop(), end = "")
print()

# Part two
input = open("Day 5/input.txt", "r")
for line in input:
    instr = line.split(" ")
    queue = []
    for i in range(int(instr[1])):
        queue.append(new_stacks_two[int(instr[3]) - 1].pop())
    for i in range(int(instr[1])):
        new_stacks_two[int(instr[5]) - 1].append(queue.pop())

print("Part two: ", end = "")
for stack in new_stacks_two:
    print(stack.pop(), end = "")