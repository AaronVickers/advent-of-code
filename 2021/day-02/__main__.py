def part1():
    file = open("input.txt")

    depth = 0
    horizontalPos = 0

    for line in file:
        command = line.split(" ")

        if command[0] == "forward":
            horizontalPos += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])

    print("Part 1:")
    print("| Depth: {0}".format(depth))
    print("| Horizontal position: {0}".format(horizontalPos))
    print("| Product: {0}".format(depth * horizontalPos))

def part2():
    file = open("input.txt")

    aim = 0
    depth = 0
    horizontalPos = 0

    for line in file:
        command = line.split(" ")

        if command[0] == "forward":
            depth += aim*int(command[1])
            horizontalPos += int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    print("Part 2:")
    print("| Depth: {0}".format(depth))
    print("| Horizontal position: {0}".format(horizontalPos))
    print("| Product: {0}".format(depth * horizontalPos))

if __name__ == "__main__":
    part1()
    part2()
