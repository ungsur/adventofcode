"""This is day 6 of advent of code"""


def processiterations(fisharr: list, iterations: int):
    """
    process fisharray the provided iterations
    and returns length of the final array
    """
    queuelen = len(fisharr)
    fishcounter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for val in fisharr:
        if fishcounter.get(val):
            fishcounter[val] += 1
        else:
            fishcounter[val] = 1
    print(fishcounter)
    for _ in range(iterations):
        for k, _ in fishcounter.items():
            fishcounter[k] -= 1
    print(fishcounter)
    return queuelen


def main():
    """
    here is my docstring
    """
    example = [3, 4, 3, 1, 2]
    print(processiterations(example, 3))


if __name__ == "__main__":
    main()
