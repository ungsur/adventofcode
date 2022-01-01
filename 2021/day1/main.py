def sweep(inputfile):
    depths = []
    with open(inputfile) as fh:
        for line in fh:
            depths.append(int(line))
    counter = 0
    for i in range(1, len(depths)):
        if depths[i-1] < depths[i]:
            counter += 1
    return counter


def sweep_part2(inputfile):
    depths = []
    with open(inputfile) as fh:
        for line in fh:
            depths.append(int(line))
    counter = 0
    newdepths = []
    for i in range(2, len(depths)):
        depthsum = sum(depths[i-2:i+1])
        newdepths.append(depthsum)
    for i in range(1, len(newdepths)):
        if newdepths[i-1] < newdepths[i]:
            counter += 1
    return counter


def main():
    inputfile = './input/exampleinput'
    print(sweep_part2(inputfile))
    inputfile2 = './input/input.txt'
    print(sweep_part2(inputfile2))


if __name__ == '__main__':
    main()
