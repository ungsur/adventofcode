""" advent of code 2022 day 1 """


def find_max(inputfile):
    """find the maximum calories"""
    with open(inputfile, encoding="utf-8") as fh:
        maxcal, tmpcal = 0, 0
        for line in fh:
            if line == "\n":
                maxcal = max(maxcal, tmpcal)
                tmpcal = 0
            else:
                tmpcal += int(line)
        return maxcal


def find_max2(inputfile):
    """find the sum of top 3 calorie counts"""
    with open(inputfile, encoding="UTF-8") as fh:
        cal_arr = []
        tmpcal = 0
        for line in fh:
            if line == "\n":
                cal_arr.append(tmpcal)
                tmpcal = 0
            else:
                tmpcal += int(line)
        cal_arr.sort()
        print(cal_arr)
        return sum(cal_arr[-3:])


def main():
    """main function"""
    examplefile = "./input/example.txt"
    inputfile1 = "./input/input1.txt"
    print(find_max(examplefile))
    print(find_max(inputfile1))
    print(find_max2(examplefile))
    print(find_max2(inputfile1))


if __name__ == "__main__":
    main()
