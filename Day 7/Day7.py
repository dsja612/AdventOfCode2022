input = open("Day 7/input.txt", "r")

dirs = {}
dirSize = {}

# Input parsing
curDir = []
for line in input:
    parsed = line.removesuffix("\n").split(" ")

    # Parsing commands
    if parsed[0] == "$":
        if parsed[1] == "cd":
            if parsed[2] == "..":
                curDir.pop()
            else:
                curDir.append(parsed[2])
                dirString = "/".join(curDir)
                if dirString not in dirs:
                    dirs[dirString] = {}
                    dirs[dirString]["files"] = []
                    dirs[dirString]["dirs"] = []
        else:
            pass #pass if LS
    # Parsing files/dirs
    else:
        dirString = "/".join(curDir)
        if parsed[0] == "dir":
            dirs[dirString]["dirs"].append(parsed[1])
        else:
            dirs[dirString]["files"].append(int(parsed[0]))

# Part one: 
def getSize(dir):
    if dir not in dirSize:
        dirSize[dir] = 0

    for fileSize in dirs[dir]["files"]:
        dirSize[dir] += fileSize

    for d in dirs[dir]["dirs"]:
        if (dir + "/" + d) not in dirSize:
            getSize(dir + "/" + d)          
        dirSize[dir] += dirSize[dir + "/" + d]

getSize("/") # Recursively fill up space of directory

deleteableSize = 0
for dir in dirSize:
    if dirSize[dir] <= 100000:
        deleteableSize += dirSize[dir]
print("Part one: {}".format(deleteableSize))

# Part two:
sorted = dict(sorted(dirSize.items(), key=lambda x: (x[1], x[0])))
for dir in sorted:
    # Potential free space = Total space - root + deleting curr dir
    if (70000000 - sorted["/"] + sorted[dir]) >= 30000000:
        print("Part two: {}".format(sorted[dir]))
        break