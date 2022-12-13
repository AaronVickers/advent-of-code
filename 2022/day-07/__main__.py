from enum import Enum
import re

def setup(file, root):
    cwd = []

    def getCurrentDir():
        cwdDict = root

        for x in cwd:
            cwdDict = cwdDict[x]
        
        return cwdDict

    def cd(dir):
        if dir == "/":
            cwd.clear()
        elif dir == "..":
            cwd.pop()
        else:
            cwd.append(dir)

    def ls():
        for line in file:
            cmd = re.search("^\$ (.+)$", line)

            if cmd != None:
                processCmd(cmd.group(1))
                return
            
            item = line.strip().split(" ")
            
            if item[0] == "dir":
                getCurrentDir()[item[1]] = {}
            else:
                getCurrentDir()[item[1]] = int(item[0])
    
    def processCmd(cmd):
        args = cmd.split(" ")

        if args[0] == "cd":
            cd(args[1])
        elif args[0] == "ls":
            ls()
    
    for line in file:
        cmd = re.search("^\$ (.+)$", line)

        if cmd == None:
            continue
        
        processCmd(cmd.group(1))

def part1():
    root = {}
    
    with open("input.txt") as file:
        setup(file, root)
    
    def getSumOfDirsUpToSize(size):
        sumOfDirsUpToSize = 0

        def checkDirSizeRecursive(dir):
            nonlocal sumOfDirsUpToSize

            dirSize = 0

            for item in dir.values():
                try:
                    dirSize += item
                except:
                    dirSize += checkDirSizeRecursive(item)
            
            if dirSize <= size:
                sumOfDirsUpToSize += dirSize

            return dirSize
        
        checkDirSizeRecursive(root)
        
        return sumOfDirsUpToSize
    
    sumOfDirsUpTo100000 = getSumOfDirsUpToSize(100000)
    
    print("Part 1: {0}".format(sumOfDirsUpTo100000))

def part2():
    root = {}
    
    with open("input.txt") as file:
        setup(file, root)
    
    def getDirSizeRecursive(dir):
        dirSize = 0

        for item in dir.values():
            try:
                dirSize += item
            except:
                dirSize += getDirSizeRecursive(item)
        
        return dirSize
    
    rootDirSize = getDirSizeRecursive(root)
    
    sizeToClear = rootDirSize - (70000000 - 30000000)
    
    def getSizeOfSmallestDirOverSize(size):
        sizeOfSmallestDirOverSize = -1

        def checkDirSizeRecursive(dir):
            nonlocal sizeOfSmallestDirOverSize

            dirSize = 0

            for item in dir.values():
                try:
                    dirSize += item
                except:
                    dirSize += checkDirSizeRecursive(item)
            
            if dirSize > size and (dirSize < sizeOfSmallestDirOverSize or sizeOfSmallestDirOverSize < 0):
                sizeOfSmallestDirOverSize = dirSize

            return dirSize
        
        checkDirSizeRecursive(root)
        
        return sizeOfSmallestDirOverSize
    
    sizeOfSmallestSufficientDir = getSizeOfSmallestDirOverSize(sizeToClear)
    
    print("Part 2: {0}".format(sizeOfSmallestSufficientDir))

if __name__ == "__main__":
    part1()
    part2()
