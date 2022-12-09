def part1():
    prioritySum = 0

    lowerOrd = ord("a")
    upperOrd = ord("A")

    def getPriority(item):
        itemOrd = ord(item)
        
        if itemOrd >= lowerOrd:
            return itemOrd - lowerOrd + 1
        else:
            return itemOrd - upperOrd + 27

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            lineLength = len(line)

            compartment1 = line[:lineLength//2]
            compartment2 = line[lineLength//2:]

            commonItem = None

            for item in compartment1:
                if item in compartment2:
                    commonItem = item
                    break
            
            prioritySum += getPriority(commonItem)
    
    print("Part 1: {0}".format(prioritySum))

def part2():
    badgePrioritySum = 0

    lowerOrd = ord("a")
    upperOrd = ord("A")

    def getPriority(item):
        itemOrd = ord(item)
        
        if itemOrd >= lowerOrd:
            return itemOrd - lowerOrd + 1
        else:
            return itemOrd - upperOrd + 27

    with open("input.txt") as file:
        for line in file:
            group = [x.strip() for x in [line, file.readline(), file.readline()]]

            commonItem = None
            
            for item in group[0]:
                if item in group[1] and item in group[2]:
                    commonItem = item
                    break
            
            badgePrioritySum += getPriority(commonItem)
    
    print("Part 2: {0}".format(badgePrioritySum))

if __name__ == "__main__":
    part1()
    part2()
