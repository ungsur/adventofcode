"""advent of code day 11"""


def get_input(filename):
    inputlist = []
    with open(filename) as filehandle:
        for line in filehandle:
            inputlist.append(list(map(int, list(line.strip()))))
    return inputlist


def addone(grid):
    flash = 0

    def _get_neighbors(grid, x, y):
        neighbors_matrix = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
        neighbors = []
        for neighbor_x, neighbor_y in neighbors_matrix:
            if 0 <= (x + neighbor_x) < len(grid) and 0 <= y + neighbor_y < len(grid):
                neighbors.append((x + neighbor_x, y + neighbor_y))
        return sorted(neighbors)

    for k in range(30000):
        flashqueue = []
        for i, _ in enumerate(grid):
            for j, _ in enumerate(grid[0]):
                grid[i][j] += 1
                if grid[i][j] > 9:
                    flashqueue.append((i, j))
        while flashqueue:
            x, y = flashqueue.pop()
            if grid[x][y] == 0:
                continue
            grid[x][y] = 0
            flash += 1
            nbors = _get_neighbors(grid, x, y)
            for nbor_x, nbor_y in nbors:
                if (
                    0 <= nbor_x < len(grid)
                    and 0 <= nbor_y < len(grid)
                    and grid[nbor_x][nbor_y] != 0
                ):
                    grid[nbor_x][nbor_y] += 1
                    if grid[nbor_x][nbor_y] > 9:
                        flashqueue.append((nbor_x, nbor_y))
        if k == 99:
            print(f"part 1: {flash}")
        if all([item == 0 for sublist in grid for item in sublist]):
            return f"Part 2: {k+1}"


def main():
    """main function definition"""
    dumbos = get_input("input/input.txt")
    print(dumbos)
    print(addone(dumbos))


if __name__ == "__main__":
    main()
