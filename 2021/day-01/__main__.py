def part1():
    file = open("input.txt")

    firstLine = True
    previousValue = 0
    increases = 0

    for line in file:
        if firstLine:
            firstLine = False
            previousValue = int(line)
        else:
            currentvalue = int(line)
            
            if currentvalue > previousValue:
                increases += 1

            previousValue = currentvalue

    print("Part 1: {0}".format(increases))

def part2():
    file = open("input.txt")

    requiredValues = 3
    acquiredValues = 0
    currentValues = []
    increases = 0

    for line in file:
        if acquiredValues < requiredValues:
            acquiredValues += 1

            currentValues.append(int(line))
        else:
            previousSum = sum(currentValues)

            currentValues.pop(0)

            currentValues.append(int(line))

            if sum(currentValues) > previousSum:
                increases += 1

    print("Part 1: {0}".format(increases))

if __name__ == "__main__":
    part1()
    part2()
