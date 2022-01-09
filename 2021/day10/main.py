"""Advent of code day 10"""


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
    return None


def bracketcheck_part2(word):
    lookup = {"}": "{", ")": "(", "]": "[", ">": "<"}
    temp_stack = []

    for letter in list(word):
        if letter in ["(", "{", "[", "<"]:
            temp_stack.append(letter)
        elif letter in [")", "}", "]", ">"]:
            brack = temp_stack.pop()
            if lookup[letter] != brack:
                return []
    return temp_stack


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


def inputsum_part2(inputlist):
    vals = {"}": 3, ")": 1, "]": 2, ">": 4}
    lookup = {"{": "}", "(": ")", "[": "]", "<": ">"}
    total = 0
    for brack in inputlist[::-1]:
        total = total * 5
        total += vals[lookup[brack]]
    return total


def main():
    inputlist = getinput("input/input.txt")
    print(inputlist)
    print(inputsum(inputlist))

    print(bracketcheck_part2("[({(<(())[]>[[{[]{<()<>>"))
    print(inputsum_part2(bracketcheck_part2("<{([{{}}[<[[[<>{}]]]>[]]")))
    stacks = []
    for bracketline in inputlist:
        total = inputsum_part2(bracketcheck_part2(bracketline))
        if total > 0:
            stacks.append(total)
    mid = len(stacks) // 2
    print(sorted(stacks))
    print(sorted(stacks)[mid])


if __name__ == "__main__":
    main()
