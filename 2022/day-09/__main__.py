def part1():
    headPosition = [0, 0]
    tailPosition = [0, 0]
    tailVisitedSet = set([tuple(tailPosition)])

    def moveHeadUp():
        headPosition[1] += 1

    def moveHeadDown():
        headPosition[1] -= 1

    def moveHeadLeft():
        headPosition[0] -= 1

    def moveHeadRight():
        headPosition[0] += 1

    def updateTailPosition():
        offsetX = headPosition[0] - tailPosition[0]
        offsetY = headPosition[1] - tailPosition[1]

        offsetAbsX = abs(offsetX)
        offsetAbsY = abs(offsetY)

        if offsetAbsX + offsetAbsY == 3:
            tailPosition[0] += 1 if offsetX > 0 else -1
            tailPosition[1] += 1 if offsetY > 0 else -1
        elif offsetAbsX == 2:
            tailPosition[0] += offsetX // 2
        elif offsetAbsY == 2:
            tailPosition[1] += offsetY // 2

    with open("input.txt") as file:
        for line in file:
            move = line.strip().split(" ")
            moveHeadFunction = None
            
            if move[0] == "U":
                moveHeadFunction = moveHeadUp
            elif move[0] == "D":
                moveHeadFunction = moveHeadDown
            elif move[0] == "L":
                moveHeadFunction = moveHeadLeft
            else:
                moveHeadFunction = moveHeadRight
            
            for _ in range(0, int(move[1])):
                moveHeadFunction()
                updateTailPosition()

                tailVisitedSet.add(tuple(tailPosition))
    
    print("Part 1: {0}".format(len(tailVisitedSet)))

def part2():
    with open("input.txt") as file:
        pass

    print("Part 2: {0}".format(0))

if __name__ == "__main__":
    part1()
    part2()
