def main():
    file = open("input.txt")

    firstLine = True
    previousValue = 0
    increases = 0

    for line in file:
        if firstLine:
            firstLine = False
            previousValue = int(line)
        else:
            currentvalue = int(line)
            
            if currentvalue > previousValue:
                increases += 1

            previousValue = currentvalue

    print("Increases: {0}".format(increases))

if __name__ == "__main__":
    main()
