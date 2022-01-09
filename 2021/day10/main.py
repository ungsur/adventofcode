"""Advent of code day 10"""


from sys import base_exec_prefix


def getinput(inputfile):
    inputlist = []
    with open(inputfile) as f_handle:
        for line in f_handle:
            inputlist.append(line.strip())
    return inputlist


def bracketcheck(word):
    lookup = {"}": "{", ")": "(", "]": "[", ">": "<"}
    temp_stack = []

    for letter in list(word):
        if letter in ["(", "{", "[", "<"]:
            temp_stack.append(letter)
        elif letter in [")", "}", "]", ">"]:
            brack = temp_stack.pop()
            if lookup[letter] != brack:
                return letter


def inputsum(inputlist):
    vals = {"}": 1197, ")": 3, "]": 57, ">": 25137}
    totalsum = 0
    badbrackets = []
    for word in inputlist:
        badbrackets.append(bracketcheck(word))
    for letter in badbrackets:
        if letter:
            totalsum += vals[letter]
    return totalsum


def main():
    inputlist = getinput("input/input.txt")
    print(inputlist)
    print(inputsum(inputlist))


if __name__ == "__main__":
    main()
