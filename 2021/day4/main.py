class Board: 
    boardserial = 1
    def __init__(self,  boardarr: list[list[int]]):
        self.boardarr = boardarr
        self.boardnum = Board.boardserial
        self.boardarrt = list(map(list, zip(*boardarr)))
        Board.boardserial += 1
    

    def mark(self, num):
        for i, row in enumerate(self.boardarr):
            for j, column in enumerate(row):
                if column == num:
                    self.boardarr[i][j] = 'X'
                    self.boardarrt[j][i] = 'X'
        return self

    def check_winner(self):
        for i, row in enumerate(self.boardarr):
            for j, num in enumerate(row):
                if all(element == 'X' for element in self.boardarr[i][:]):
                    return self.boardnum, Board(self.boardarr)
                if all(element == 'X' for element in self.boardarrt[j][:]):
                    return self.boardnum, Board(self.boardarrt)
        return False
    
    
    def boardsum(self):
        total = 0
        for row in self.boardarr:
            for col in row:
                if col == 'X':
                    pass
                else:
                    total += col
        return total


    def __repr__(self):
            return f'Board Number:{self.boardnum}, Board:  {self.boardarr}, BoardT: {self.boardarrt}'


def process_input(filename):
    with open(filename) as fh:
        balls = fh.readline()
        balls = (list(map(int,balls.strip().split(','))))
        boardsarr = fh.readlines()
    boardlist = []
    tmpboard = []
    i = 0
    while i < len(boardsarr):
        if boardsarr[i] == '\n':
            if tmpboard == []:
                pass
            else:
                boardlist.append(tmpboard)
                tmpboard = []
        else:
            tmpboard.append(list(map(int,boardsarr[i].strip().split())))
        i += 1
    boardlist.append(tmpboard)
    
    return balls, boardlist

def play_bingo(balls, boardlist):
    for ball in balls:
        for board in boardlist:
            board.mark(ball)
            if board.check_winner():
                return ball * board.boardsum()
    return False

def play_bingo_part2(balls, boardlist):
    winnerlist = []
    winnersum = []
    winnerball = []
    for ball in balls:
        for board in boardlist:
            board.mark(ball)
            if board.check_winner() and board.boardnum not in winnerlist:
                winningboard = board.check_winner()
                winnerlist.append(board.boardnum)
                winnersum.append(board.boardsum())
                winnerball.append(ball)
    return winnersum[-1] * winnerball[-1]
    
def main():
    inputfile = "./input/input.txt"
    ballnums, boards = process_input(inputfile)
    a = ballnums
    blist = []
    for board in boards:
        blist.append(Board(board))
    print('Part 1 answer: ', play_bingo(a,blist))
    print('Part 2 answer: ', play_bingo_part2(a,blist))
    


if __name__ == "__main__":
    main()