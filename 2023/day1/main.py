""" advent of code 2023 day 1 """


def find_numbers(inputfile):
    '''print out numbers in inputfile'''
    with open("input/" + inputfile, encoding='utf-8') as fh:
        total = 0
        for line in fh:
            for letter in list(line):
                if letter.isdigit():
                    firstdigit = letter
                    break
            for letter in list(line)[::-1]:
                if letter.isdigit():
                    lastdigit = letter
                    break
            total += (int(firstdigit+lastdigit))
        print(total)


def find_number_2024(inputfile):
    '''prints out sum of digits in inputfile'''
    with open('input/'+inputfile, encoding='utf-8') as fh:
        total = 0
        for line in fh:
            for letter in list(line):
                if letter.isdigit():
                    firstdigit = letter
                    break
            for letter in list(line)[::-1]:
                if letter.isdigit():
                    lastdigit = letter
                    break
            total += int(firstdigit+lastdigit)
        return(total)


numbers = ['zero',
           'one',
           'two',
           'three'
           'four',
           'five',
           'six',
           'seven',
           'eight',
           'nine']


def get_first(s: str) -> int:
    '''get first number in string'''
    for i, c in enumerate(s):
        if c.isdigit():
            return int(c)
        else:
            for num in numbers:
                if s[i:].startswith(num):
                    return numbers.index(num)


def get_last(s: str) -> int:
    '''get last number in string'''
    for i, c in enumerate(reversed(s)):
        if c.isdigit():
            return int(c)
        else:
            for num in numbers:
                if s[-(i+1):].startswith(num):
                    return numbers.index(num)


def convert_nums(inputfile):
    '''print out numbers in inputfile'''
    total = 0
    with open("input/" + inputfile, encoding='utf-8') as fh:
        lines = []
        for line in fh:
            lines.append(line.strip())
    for line in lines:
        total += 10*get_first(line)+get_last(line)
    return total


def convert_nums_2024(inputfile):
    numbers = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9,
               'zero': 0
               }
    def _getfirst(s:str) -> int:
        for i, letter in enumerate(s): # abcone2threexyz
            if letter.isdigit():
                return int(letter)
            else:
                for num in numbers.keys():
                    if s[i:].startswith(num):
                        return numbers[num]
                    
    def _getlast(s:str) -> int:
        for i, letter in enumerate(reversed(s)):
            if letter.isdigit():
                return int(letter)
            else:
                for num in numbers.keys():
                    if s[-(i+1):].startswith(num):
                        return numbers[num]

    with open("input/" + inputfile, encoding='utf8') as fh:
        total = 0
        for line in fh:
            total += (10*_getfirst(line)+_getlast(line))
        return total
                  
def main():
    """main function"""
    '''print(find_numbers("input1.txt"))'''
    '''print(convert_nums("input1.txt"))'''
    '''print(find_number_2024("input1.txt"))'''
    print(convert_nums_2024("input1.txt"))


if __name__ == '__main__':
    main()
