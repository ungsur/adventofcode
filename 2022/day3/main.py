'''advent of code day 3'''
from collections import defaultdict

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
    with open(inputfile, encoding='UTF-8') as fh:
        for i,line in enumerate(fh):
            print(i,set(line))
            arr = list(line)
            if i % 3:
                lettersdict = defaultdict(1)
                for letter in arr:
                    lettersdict['letter'] += 1
                else:
                    lettersdict[letter] +=1
                print(lettersdict)
    return total

def main():
    '''the main func'''
    inputfile = 'input/example.txt'
    inputfile = 'input/input1.txt'
    print(find_groups(inputfile))


if __name__ == '__main__':
    main()
