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

if __name__ == "__main__":
    part1()
