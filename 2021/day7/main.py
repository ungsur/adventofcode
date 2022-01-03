"""This is advent of code day 7"""


def getinput(file):
    """docstring to get inputlist function"""
    with open(file) as filehandle:
        crabs = filehandle.readline().split(",")
        crabs = list(map(int, crabs))
    return crabs


def findlowestfuel(crabarr):
    """find the lowest amount of fuel to lineup crabs"""
    crabarr = sorted(crabarr)
    ans = {}
    maxcrab = max(crabarr)
    for i in range(maxcrab):
        tmparr = []
        for _, num in enumerate(crabarr):
            tmparr.append(abs(num - i))
        # print(tmparr, sum(tmparr), i)
        ans[sum(tmparr)] = i
    return min(ans.keys())


def findlowestfuel_part2(crabarr):
    """find the lowest amount of fuel to lineup crabs"""
    crabarr.sort()
    ans = {}
    maxcrab = max(crabarr)
    for i in range(maxcrab):
        tmparr = []
        for _, num in enumerate(crabarr):
            tmparr.append(calculatestep(abs(num - i) + 1))
        # print(tmparr, sum(tmparr), i)
        ans[sum(tmparr)] = i
    return min(ans.keys())


def calculatestep(distance: int) -> int:
    """calculate step for part 2"""
    totalsum = 0
    for i in range(1, distance):
        totalsum += i
    return totalsum


def main():
    """main docstring"""
    example = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    print(sorted(example))
    print(sum(example) / len(example))
    print(f"part 1 min fuel for example: {findlowestfuel(example)}")
    crabs = getinput("input/input.txt")
    print(f"part 2 min fuel for example: {findlowestfuel_part2(crabs)}")


if __name__ == "__main__":
    main()
