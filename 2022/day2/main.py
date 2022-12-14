'''day 2 advent of code 2022'''


def wincheck(first, second):
    '''get win result'''
    if second == first:
        return 3
    elif second == 'Rock' and first == 'Scissors':
        return 6
    elif second == 'Paper' and first == 'Rock':
        return 6
    elif second == 'Scissors' and first == 'Paper':
        return 6
    else:
        return 0


def wincheck2(first, second):
    '''get result after 2nd part'''
    if second == 'X':
        return 0
    if second == 'Y':
        return 3
    if second == 'Z':
        return 6


def valcheck(letter):
    if letter == 'Rock':
        return 1
    elif letter == 'Paper':
        return 2
    elif letter == 'Scissors':
        return 3


def valcheck2(first, second):
    winner_dict = {'Rock': 'Paper',
                    'Paper': 'Scissors',
                    'Scissors': 'Rock'}
    loser_dict = { 'Rock': 'Scissors',
                   'Paper': 'Rock',
                   'Scissors': 'Paper'}

    if second == 'X':
        return valcheck(loser_dict[first])
    elif second == 'Y':
        return valcheck(first)
    elif second == 'Z':
        return valcheck(winner_dict[first])

def translate_hand(letter):
    '''translate letter into hand of RPS'''
    lookup_dict = { 'A': 'Rock',
                    'B': 'Paper',
                    'C': 'Scissors',
                    'X': 'Rock',
                    'Y': 'Paper',
                    'Z': 'Scissors',
                    }
    return lookup_dict[letter]


def calculate_score(inputfile):
    '''find the score after trying strategy'''
    score = 0

    with open(inputfile, encoding='utf-8') as fh:
        for line in fh:
            first, second = line.split()
            score += wincheck(translate_hand(first), translate_hand(second)) + valcheck(translate_hand(second))
    return score


def calculate_score2(inputfile):
    '''find the score after trying strategy'''
    score = 0

    with open(inputfile, encoding='utf-8') as fh:
        for line in fh:
            first, second = line.split()
            print(wincheck2(first, second), valcheck2(translate_hand(first), second), first, second)
            score += wincheck2(first, second) + valcheck2(translate_hand(first), second)
    return score


def main():
    '''do main()'''
    examplefile = './input/example.txt'
    inputfile = './input/input1.txt'
    print(calculate_score(inputfile))
    print(wincheck2('B', 'Z')+ valcheck2(translate_hand('B'),'Z'))
    print(calculate_score2(inputfile))


if __name__ == '__main__':
    main()
