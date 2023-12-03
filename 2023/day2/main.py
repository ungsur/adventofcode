""" advent of code 2023 day 2 """


def count_cubes(inputfile):
    '''print out numbers in inputfile'''

    def process_game(gamestr):
        print(gamestr.strip())
        cube_limits = {'red': 12, 'green': 13, 'blue': 14}

        gamenum = int(gamestr.strip('\n').split(':')[0].split('Game ')[1])
        gamesets = gamestr.strip('\n').split(': ')[1].split('; ')
        for game in gamesets:
            cube_limits = {'red': 12, 'green': 13, 'blue': 14}
            thingstack = []
            for thing in game.split(','):
                thingstack.append(thing.split())
            while thingstack:
                ballnum, ballcol = thingstack.pop()
                cube_limits[ballcol] -= int(ballnum)
                print(cube_limits)
                if cube_limits[ballcol] < 0:
                    return 0
            print(gamenum)
        return gamenum

    def process_powers(gamestr):
        gamesets = gamestr.strip('\n').split(': ')[1].split('; ')
        print("game: ", gamesets)
        cube_powers = {}
        for game in gamesets:
            thingstack = []
            for thing in game.split(','):
                thingstack.append(thing.split())
            while thingstack:
                ballnum, ballcol = thingstack.pop()
                if cube_powers.get(ballcol):
                    if cube_powers[ballcol] < int(ballnum):
                        cube_powers[ballcol] = int(ballnum)
                else:
                    cube_powers[ballcol] = int(ballnum)
        print("cubepowers: ", cube_powers)
        powertotal = 1
        for k,v in cube_powers.items():
            powertotal *= v
        print(powertotal)
        return powertotal

    with open("input/" + inputfile, encoding='UTF-8') as fh:
        total = 0
        powertotal = 0

        for line in fh:
            # total += process_game(line.strip('\''))
            powertotal += process_powers(line.strip('\''))
        return powertotal


def main():
    """main function"""
    '''print(count_cubes("input1.txt"))'''
    print(count_cubes("input1.txt"))

if __name__ == '__main__':
    main()
