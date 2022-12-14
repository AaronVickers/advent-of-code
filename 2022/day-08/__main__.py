def part1():
    treeGrid = []
    visibleTreeGrid = []

    with open("input.txt") as file:
        for line in file:
            treeGridLine = [int(treeHeight) for treeHeight in list(line.strip())]

            treeGrid.append(treeGridLine)
            visibleTreeGrid.append([0] * len(treeGridLine))
    
    treeGridY = len(treeGrid)
    treeGridX = len(treeGrid[0])
    
    for y in range(0, treeGridY):
        currentHighest = -1

        for x in range(0, treeGridX):
            treeHeight = treeGrid[y][x]

            if treeHeight > currentHighest:
                currentHighest = treeHeight

                visibleTreeGrid[y][x] = 1
    
    for y in range(0, treeGridY):
        currentHighest = -1

        for x in reversed(range(0, treeGridX)):
            treeHeight = treeGrid[y][x]

            if treeHeight > currentHighest:
                currentHighest = treeHeight

                visibleTreeGrid[y][x] = 1
    
    for x in range(0, treeGridX):
        currentHighest = -1

        for y in range(0, treeGridY):
            treeHeight = treeGrid[y][x]

            if treeHeight > currentHighest:
                currentHighest = treeHeight

                visibleTreeGrid[y][x] = 1
    
    for x in range(0, treeGridX):
        currentHighest = -1

        for y in reversed(range(0, treeGridY)):
            treeHeight = treeGrid[y][x]

            if treeHeight > currentHighest:
                currentHighest = treeHeight

                visibleTreeGrid[y][x] = 1

    visibleTrees = sum(visibleTreeGridRow.count(1) for visibleTreeGridRow in visibleTreeGrid)
    
    print("Part 1: {0}".format(visibleTrees))

def part2():
    treeGrid = []

    with open("input.txt") as file:
        for line in file:
            treeGrid.append([int(treeHeight) for treeHeight in list(line.strip())])
    
    treeGridY = len(treeGrid)
    treeGridX = len(treeGrid[0])
    
    def calculateScenicScore(treeX, treeY):
        treeHeight = treeGrid[treeY][treeX]

        visibleTreesUp = 0

        for y in range(treeY-1, -1, -1):
            visibleTreesUp += 1

            if treeGrid[y][treeX] >= treeHeight:
                break
        
        visibleTreesLeft = 0

        for x in range(treeX-1, -1, -1):
            visibleTreesLeft += 1

            if treeGrid[treeY][x] >= treeHeight:
                break
        
        visibleTreesDown = 0

        for y in range(treeY+1, treeGridY):
            visibleTreesDown += 1

            if treeGrid[y][treeX] >= treeHeight:
                break
        
        visibleTreesRight = 0

        for x in range(treeX+1, treeGridX):
            visibleTreesRight += 1

            if treeGrid[treeY][x] >= treeHeight:
                break
        
        return visibleTreesUp * visibleTreesLeft * visibleTreesDown * visibleTreesRight

    highestScenicScore = 0

    for y in range(0, treeGridY):
        for x in range(0, treeGridX):
            scenicScore = calculateScenicScore(x, y)

            if scenicScore > highestScenicScore:
                highestScenicScore = scenicScore
    
    print("Part 2: {0}".format(highestScenicScore))

if __name__ == "__main__":
    part1()
    part2()
