def main():
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

    print("Depth: {0}".format(depth))
    print("Horizontal position: {0}".format(horizontalPos))
    print("Product: {0}".format(depth * horizontalPos))

if __name__ == "__main__":
    main()
