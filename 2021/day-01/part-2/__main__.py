def main():
    file = open("input.txt")

    requiredValues = 3
    acquiredValues = 0
    currentValues = []
    increases = 0

    for line in file:
        if acquiredValues < requiredValues:
            acquiredValues += 1

            currentValues.append(int(line))
        else:
            previousSum = sum(currentValues)

            currentValues.pop(0)

            currentValues.append(int(line))

            if sum(currentValues) > previousSum:
                increases += 1

    print("Increases: {0}".format(increases))

if __name__ == "__main__":
    main()
