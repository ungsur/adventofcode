"""This is day 6 of advent of code"""

from collections import defaultdict


def processiterations(fisharr: list, iterations: int):
    """
    process fisharray the provided iterations
    and returns length of the final array
    """
    fishcounter = defaultdict(int)
    for val in fisharr:
        fishcounter[val] += 1
    print(fishcounter)
    for _ in range(iterations):

        ans = defaultdict(int)
        for k, cnt in fishcounter.items():
            if k == 0:
                ans[6] += cnt
                ans[8] += cnt
            else:
                ans[k - 1] += cnt
        fishcounter = ans
    return sum(ans.values())


def main():
    """define input and run processiterations with input and number of days"""
    # example = [3, 4, 3, 1, 2]
    inputlist = [
        1,
        1,
        1,
        1,
        3,
        1,
        4,
        1,
        4,
        1,
        1,
        2,
        5,
        2,
        5,
        1,
        1,
        1,
        4,
        3,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        2,
        4,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        1,
        1,
        5,
        1,
        1,
        2,
        1,
        5,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        4,
        3,
        1,
        1,
        1,
        2,
        1,
        1,
        5,
        2,
        1,
        1,
        1,
        1,
        4,
        5,
        1,
        1,
        2,
        4,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        1,
        5,
        1,
        3,
        1,
        1,
        4,
        2,
        1,
        5,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        3,
        3,
        1,
        5,
        1,
        1,
        1,
        1,
        3,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        4,
        1,
        4,
        3,
        1,
        1,
        1,
        4,
        1,
        2,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        3,
        5,
        1,
        1,
        5,
        2,
        1,
        1,
        1,
        1,
        1,
        4,
        4,
        1,
        1,
        2,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        5,
        3,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        4,
        1,
        4,
        1,
        1,
        1,
        5,
        1,
        1,
        3,
        2,
        2,
        1,
        1,
        1,
        4,
        1,
        3,
        1,
        1,
        1,
        2,
        1,
        3,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        1,
        1,
        2,
        1,
        4,
        1,
        1,
        1,
        1,
        1,
        4,
        1,
        1,
        2,
        4,
        2,
        1,
        2,
        3,
        1,
        3,
        1,
        1,
        2,
        1,
        1,
        1,
        3,
        1,
        1,
        3,
        1,
        1,
        4,
        1,
        3,
        1,
        1,
        2,
        1,
        1,
        1,
        4,
        1,
        1,
        3,
        1,
        1,
        5,
        1,
        1,
        3,
        1,
        1,
        1,
        1,
        5,
        1,
        1,
        1,
        1,
        1,
        2,
        3,
        4,
        1,
        1,
        1,
        1,
        1,
        2,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        3,
        2,
        2,
        1,
        3,
        5,
        1,
        1,
        4,
        4,
        1,
        3,
        4,
        1,
        2,
        4,
        1,
        1,
        3,
        1,
    ]
    print(processiterations(inputlist, 80))
    print(processiterations(inputlist, 256))


if __name__ == "__main__":
    main()
