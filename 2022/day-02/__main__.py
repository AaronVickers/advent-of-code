def part1():
    totalScore = 0

    lowerOrd = ord('A')
    upperOrd = ord('X')

    with open("input.txt") as file:
        for line in file:
            moves = line.strip().split(" ")
            moves[0] = ord(moves[0]) - lowerOrd + 1
            moves[1] = ord(moves[1]) - upperOrd + 1

            movesDiff = moves[1] - moves[0]

            score = moves[1] + (6 if movesDiff == 1 or movesDiff == -2 else 3 if movesDiff == 0 else 0)

            totalScore += score
    
    print("Part 1: {0}".format(totalScore))

def part2():
    totalScore = 0

    lowerOrd = ord('A')
    upperOrd = ord('X')

    def wrapMove(move):
        return 1 + (move - 1) % (4 - 1)

    with open("input.txt") as file:
        for line in file:
            round = line.strip().split(" ")
            round[0] = ord(round[0]) - lowerOrd + 1
            round[1] = ord(round[1]) - upperOrd + 1

            move = wrapMove(round[0]-1) if round[1] == 1 else round[0] if round[1] == 2 else wrapMove(round[0]+1)

            score = move + (0 if round[1] == 1 else 3 if round[1] == 2 else 6)


            totalScore += score
    
    print("Part 2: {0}".format(totalScore))

if __name__ == "__main__":
    part1()
    part2()
