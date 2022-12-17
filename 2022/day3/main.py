'''advent of code day 3'''


def check(inputfile):
    '''check the thing'''
    total = 0
    with open(inputfile, encoding='UTF-8') as fh:
        for line in fh:
            llen = len(line.strip())
            arr = list(line.strip())
            arr1 = arr[:llen//2]
            arr2 = arr[llen//2:]
            for letter in arr2:
                if letter in arr1:
                    if letter.islower():
                        total += ord(letter)-96
                        break
                    else:
                        total += ord(letter)-38
                        break
    return total


def find_groups(inputfile):
    '''check the groups'''
    total = 0
    letterslist = []
    lettersdict = {}
    with open(inputfile, encoding='UTF-8') as fh:
        for i, line in enumerate(fh):
            arr = list(set(line.strip()))
            if i % 3 == 0:
                lettersdict = {}
            for letter in arr:
                if lettersdict.get(letter):
                    lettersdict[letter] += 1
                else:
                    lettersdict[letter] = 1
            if i % 3 == 2:
                letterslist.append(list(lettersdict.keys())[list(lettersdict.values()).index(3)])
    print(letterslist)
    for letter in letterslist:
        if letter.islower():
            total += ord(letter)-96
        else:
            total += ord(letter)-38
    return total


def main():
    '''the main func'''
    inputfile = 'input/example.txt'
    inputfile = 'input/input1.txt'
    print(check(inputfile))
    print(find_groups(inputfile))


if __name__ == '__main__':
    main()
