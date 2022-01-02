def processiterations(fisharr: list, n: int):
    queuelen = len(fisharr)
    fishcounter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for val in fisharr:
        if fishcounter.get(val):
            fishcounter[val] += 1
        else:
            fishcounter[val] = 1
    print(fishcounter)
    for i in range(n):
        for k, v in fishcounter.items():
            fishcounter[k] -= 1
    print(fishcounter)
    return queuelen


def main():
    example = [3, 4, 3, 1, 2]
    print("hi")
    processiterations(example, 1)


if __name__ == "__main__":
    main()
