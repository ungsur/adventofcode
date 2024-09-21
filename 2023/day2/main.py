""" advent of code 2023 day 2 """
import typing as t
from dataclasses import dataclass, field


@dataclass
class Round:
    red: int = 0
    blue: int = 0
    green: int = 0

    @classmethod
    def from_input(cls, text:str) -> t.Self:
        parts = [pair.strip().partition(" ") for pair in text.split(",")]
        return cls(**{name.strip(): int(value) for value, _ , name in parts})
@dataclass
class Game:
    id: int
    rounds: t.Sequence[Round]

    @classmethod
    def from_line(cls, line:str) -> t.Self:
        identifier, _, remainder = line.partition(":")
        number = int(identifier.split()[1])
        rounds = [Round.from_input(part.strip()) for part in remainder.split(";")]
        return cls(number, tuple(rounds))
    
    def is_possible(self, red: int, green: int, blue: int)->bool:
        return all(round.red<=red and round.green <= green and round.blue <= blue
                   for round in self.rounds
                   )
    

class PowerGame(Game):
    @property
    def power(self) -> int:
        red = green = blue = 0
        for round in self.rounds:
            red = max(red, round.red)
            green = max(green, round.green)
            blue = max(blue, round.blue)
        return red * green * blue
    

def count_cubes_2024(inputfile):
    '''print sum of ID's for valid games'''


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
    import aocd
    games =  [Game.from_line(line) for line in aocd.get_data(day=2, year=2023).splitlines()]
    print(sum(game.id for game in games if game.is_possible(12, 13, 14)))
    
    games =  [PowerGame.from_line(line) for line in aocd.get_data(day=2, year=2023).splitlines()]
    print(sum(game.power for game in games))
    
    """main function"""
    '''print(count_cubes("input1.txt"))'''
    #print(count_cubes("input1.txt"))

if __name__ == '__main__':
    main()
