import re

def setup(file, stacks):
    numStacks = 0

    for line in file:
        numCrates = 0

        for x in range(0, len(line), 4):
            stackIndex = x//4

            if stackIndex+1 > numStacks:
                numStacks = stackIndex+1
                stacks.append([])
            
            stackSlot = line[x:x+3]
            
            crate = re.search("^\[([A-Z])\]$", stackSlot)
            
            if crate == None:
                continue

            stacks[stackIndex].insert(0, crate.group(1))
            numCrates += 1
        
        if numCrates == 0:
            break

def part1():
    stacks = []
    message = ""

    with open("input.txt") as file:
        setup(file, stacks)
        
        for line in file:
            instruction = re.search("^move (\d+) from (\d+) to (\d+)$", line)

            if instruction == None:
                continue
            
            for x in range(int(instruction.group(1))):
                crate = stacks[int(instruction.group(2))-1].pop()

                stacks[int(instruction.group(3))-1].append(crate)

    for stack in stacks:
        message += stack[len(stack)-1]
    
    print("Part 1: {0}".format(message))

def part2():
    numStacks = 0
    stacks = []
    message = ""

    with open("input.txt") as file:
        setup(file, stacks)
        
        for line in file:
            instruction = re.search("^move (\d+) from (\d+) to (\d+)$", line)

            if instruction == None:
                continue

            pickedUpCrates = []
            
            for x in range(int(instruction.group(1))):
                crate = stacks[int(instruction.group(2))-1].pop()

                pickedUpCrates.append(crate)

            for crate in reversed(pickedUpCrates):
                stacks[int(instruction.group(3))-1].append(crate)

    for stack in stacks:
        message += stack[len(stack)-1]
    
    print("Part 2: {0}".format(message))

if __name__ == "__main__":
    part1()
    part2()
