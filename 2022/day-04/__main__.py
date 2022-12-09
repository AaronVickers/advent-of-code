def part1():
    fullOverlaps = 0

    with open("input.txt") as file:
        for line in file:
            sections = [[int(bound) for bound in section.split("-")] for section in line.strip().split(",")]
            
            if sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]:
                fullOverlaps += 1
            elif sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]:
                fullOverlaps += 1

    print("Part 1: {0}".format(fullOverlaps))

def part2():
    overlaps = 0

    with open("input.txt") as file:
        for line in file:
            sections = [[int(bound) for bound in section.split("-")] for section in line.strip().split(",")]
            
            if sections[0][0] >= sections[1][0] and sections[0][1] <= sections[1][1]:
                overlaps += 1
            elif sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1]:
                overlaps += 1
            elif sections[0][0] >= sections[1][0] and sections[0][0] <= sections[1][1]:
                overlaps += 1
            elif sections[0][1] >= sections[1][0] and sections[0][1] <= sections[1][1]:
                overlaps += 1
            elif sections[0][0] <= sections[1][0] and sections[0][0] >= sections[1][1]:
                overlaps += 1
            elif sections[0][1] <= sections[1][0] and sections[0][1] >= sections[1][1]:
                overlaps += 1

    print("Part 2: {0}".format(overlaps))

if __name__ == "__main__":
    part1()
    part2()
