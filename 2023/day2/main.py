""" advent of code 2023 day 2 """


def count_cubes(inputfile):
    '''print out numbers in inputfile'''

    def process_game(gamestr):
        print(gamestr.replace(";", ","))
        cube_limits = {'red': 12, 'green': 13, 'blue': 14}
        gameset = gamestr.replace(";",",").strip().split(':')[1].split(',')
        for item in gameset:
            ballnum, ballcol = item.split()
            ballnum = int(ballnum)
            cube_limits[ballcol] -= ballnum
        print(cube_limits)
        if cube_limits['red'] >= 0 and cube_limits['green'] >= 0 and cube_limits['blue'] >= 0:
            return (int(gamestr.split(":")[0].split()[1]))
        else:
            return 0

    with open("input/" + inputfile, encoding='UTF-8') as fh:
        total = 0
        for line in fh:
            total += process_game(line.strip('\''))
        return total 


def main():
    """main function"""
    print(count_cubes("input1.txt"))


if __name__ == '__main__':
    main()
