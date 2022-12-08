def part1():
    elves = [0]
    index = 0

    with open("input.txt") as file:
        for line in file:
            try:
                elves[index] += int(line)
            except:
                index += 1
                elves.append(0)
    
    print("Part 1: {0}".format(max(elves)))

def part2():
    numTopElves = 3
    topElves = [0] * numTopElves
    current = 0
    
    def tryReplaceTopElves(calories):
        replaced = False
        previous = 0

        for i in range(numTopElves):
            if replaced:
                currentPrevious = previous
                previous = topElves[i]
                topElves[i] = currentPrevious
            elif calories > topElves[i]:
                replaced = True

                previous = topElves[i]
                topElves[i] = calories

    with open("input.txt") as file:
        for line in file:
            try:
                current += int(line)
            except:
                tryReplaceTopElves(current)
                current = 0
        
        tryReplaceTopElves(current)
    
    print("Part 2: {0}".format(sum(topElves)))

if __name__ == "__main__":
    part1()
    part2()
