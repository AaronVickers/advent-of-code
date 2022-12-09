def part1():
    packetStartMarker = 0

    with open("input.txt") as file:
        index = 0
        last4 = []

        datastream = file.readline()

        for char in datastream:
            if len(last4) == 4:
                last4[index%4] = char

                if len(last4) == len(set(last4)):
                    break
            else:
                last4.append(char)

            index += 1
        
        packetStartMarker = index + 1

    print("Part 1: {0}".format(packetStartMarker))

def part2():
    messageStartMarker = 0

    with open("input.txt") as file:
        index = 0
        last14 = []

        datastream = file.readline()

        for char in datastream:
            if len(last14) == 14:
                last14[index%14] = char

                if len(last14) == len(set(last14)):
                    break
            else:
                last14.append(char)

            index += 1
        
        messageStartMarker = index + 1

    print("Part 2: {0}".format(messageStartMarker))

if __name__ == "__main__":
    part1()
    part2()
