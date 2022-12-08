def part1():
    file = open("input.txt")

    bits = {}

    for line in file:
        bitPos = 0

        for bit in line:
            if bit == '\n':
                continue
            
            if bitPos not in bits:
                bits[bitPos] = 0

            if bit == '0':
                bits[bitPos] -= 1
            else:
                bits[bitPos] += 1

            bitPos += 1
    
    gammaRateStringArray = []
    epsilonRateStringArray = []
    
    for key, value in bits.items():
        if value < 0:
            gammaRateBit = '0'
            epsilonRateBit = '1'
        else:
            gammaRateBit = '1'
            epsilonRateBit = '0'
        
        gammaRateStringArray.insert(key, gammaRateBit)
        epsilonRateStringArray.insert(key, epsilonRateBit)
    
    gammaRateString = "".join(gammaRateStringArray)
    gammaRate = int(gammaRateString, 2)

    epsilonRateString = "".join(epsilonRateStringArray)
    epsilonRate = int(epsilonRateString, 2)
    
    print("Part 1:")
    print("| Gamma rate: {0} ({1})".format(gammaRate, gammaRateString))
    print("| Epsilon rate: {0} ({1})".format(epsilonRate, epsilonRateString))
    print("| Product: {0}".format(gammaRate * epsilonRate))

if __name__ == "__main__":
    part1()
