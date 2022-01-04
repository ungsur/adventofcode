"""docstring for stupid function"""

from collections import defaultdict


def getinput_part1(filename: str):
    """docstring for stupid function"""
    filelist = []
    with open(filename) as filehandle:
        for line in filehandle:
            filelist.append(line.strip().split("|")[1].split())
    return filelist


def getinput_part2(filename: str) -> list:
    """docstring for stupid function"""
    filelist = []
    codes = []
    with open(filename) as filehandle:
        for line in filehandle:
            filelist.append(line.strip().split("|")[0].split())
            codes.append(line.strip().split("|")[1].split())
    return (filelist, codes)


def count_digits(listofcodes):
    """docstring for stupid function"""
    counter = 0
    listofcodes = [word for line in listofcodes for word in line]
    for code in listofcodes:
        if len(code) in [2, 3, 4, 7]:  # 1,7,4,8
            counter += 1
    return counter


def make_digits(transtable, codelist):
    """docstring for stupid function"""
    digits = {
        "abcefg": 0,
        "cf": 1,
        "acdeg": 2,
        "acdfg": 3,
        "bcdf": 4,
        "abdfg": 5,
        "abdefg": 6,
        "acf": 7,
        "abcdefg": 8,
        "abcdfg": 9,
    }
    digit = []
    for code in codelist:
        digit.append(digits["".join(sorted(code.translate(transtable)))])
    return "".join(list(map(str, digit)))


def make_table(code):
    """docstring for stupid function"""
    A = defaultdict()
    for word in code:
        if len(word) == 2:
            A["cf"] = set(list(word))
    for word in code:
        if len(word) == 3:
            A["a"] = set(list(word)) - A["cf"]
    for word in code:
        if len(word) == 4:
            A["bd"] = set(list(word)) - A["cf"]
    for word in code:
        if len(word) == 6:
            word = set(list(word))
            if (
                A["cf"].issubset(word)
                and A["bd"].issubset(word)
                and A["a"].issubset(word)
            ):
                A["g"] = word - A["cf"] - A["bd"] - A["a"]
    for word in code:
        if len(word) == 5:
            word = set(list(word))
            if (
                A["cf"].issubset(word)
                and A["a"].issubset(word)
                and A["g"].issubset(word)
            ):
                A["d"] = word - A["cf"] - A["g"] - A["a"]
                A["b"] = A["bd"] - A["d"]
    for word in code:
        if len(word) == 7:
            word = set(list(word))
            A["e"] = word - A["cf"] - A["bd"] - A["g"] - A["a"]
    for word in code:
        if len(word) == 6:
            word = set(list(word))
            if (
                A["e"].issubset(word)
                and A["bd"].issubset(word)
                and A["a"].issubset(word)
                and A["g"].issubset(word)
            ):
                A["f"] = word - A["e"] - A["bd"] - A["a"] - A["g"]
                A["c"] = A["cf"] - A["f"]
    del A["cf"]
    del A["bd"]
    before, after = [], []

    for k, vals in A.items():
        before.append(list(vals)[0])
        after.append(k)
    before = "".join(before)
    after = "".join(after)
    translationtable = word.maketrans(before, after)
    return translationtable


def main():
    """docstring for stupid function"""
    codenums = getinput_part1("input/input.txt")
    print(count_digits(codenums))
    codenums, codes = getinput_part2("input/input.txt")
    tables = list(map(lambda x: make_table(x), codenums))
    translation = list(zip(tables, codes))
    totalsum = 0
    for line in translation:
        totalsum += int(make_digits(line[0], line[1]))
    print(totalsum)


if __name__ == "__main__":
    main()
