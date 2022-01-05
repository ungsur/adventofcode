"""advent of code day 9"""


def getinput(filename: str) -> list:
    """docstring for gridmaking"""
    grid = []
    with open(filename) as gridhandle:
        for line in gridhandle:
            grid.append(list(map(int, list(line.strip()))))
    return grid


def checkpoint(grid: list[list], coordinate: tuple):
    """docstring to check if point is a lowpoint"""
    x, y = coordinate
    neighbors = []
    for neighbor_x, neighbor_y in [
        [x - 1, y],
        [x, y - 1],
        [x + 1, y],
        [x, y + 1],
    ]:
        if 0 <= neighbor_x < len(grid) and 0 <= neighbor_y < len(grid[0]):
            neighbors.append(grid[neighbor_x][neighbor_y])
    if grid[x][y] < min(neighbors):
        return grid[x][y]


def traversegrid(grid):
    """see grid"""
    ans = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if type(checkpoint(grid, (i, j))) == int:
                ans.append(checkpoint(grid, (i, j)))
    return sum(ans) + len(ans)


def main():
    """main function docstring"""
    cavern = getinput("input/example.txt")
    print(traversegrid(cavern))


if __name__ == "__main__":
    main()
