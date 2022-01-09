"""advent of code day 9"""


def getinput(filename: str) -> list:
    """docstring for gridmaking"""
    grid = []
    with open(filename) as gridhandle:
        for line in gridhandle:
            grid.append(list(map(int, list(line.strip()))))
    return grid


def checkpoint(grid, coordinate):
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
    return None


def traversegrid(grid):
    """see grid"""
    lowpoints = []
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[i]):
            if isinstance(checkpoint(grid, (i, j)), int):
                lowpoints.append(checkpoint(grid, (i, j)) + 1)
    return sum(lowpoints)


def get_lowpoints(grid):
    """see grid"""
    ans = []
    lowpoints = []
    for i, _ in enumerate(grid):
        for j in range(len(grid[i])):
            if isinstance(checkpoint(grid, (i, j)), int):
                ans.append(checkpoint(grid, (i, j)))
                lowpoints.append([i, j])
    return lowpoints


def part2(grid):
    """docstring for part 2"""
    basin_sizes = []
    seen = set()
    for x, _ in enumerate(grid):
        for y, _ in enumerate(grid[0]):
            if (x, y) not in seen and grid[x][y] != 9:
                basinsize = 0
                temp_que = []
                temp_que.append((x, y))
                while temp_que:
                    (x, y) = temp_que.pop(0)
                    if (x, y) in seen:
                        continue
                    seen.add((x, y))
                    basinsize += 1
                    for neighbor_x, neighbor_y in [
                        [x - 1, y],
                        [x, y - 1],
                        [x + 1, y],
                        [x, y + 1],
                    ]:
                        if (
                            0 <= neighbor_x < len(grid)
                            and 0 <= neighbor_y < len(grid[0])
                            and grid[neighbor_x][neighbor_y] != 9
                        ):
                            temp_que.append((neighbor_x, neighbor_y))
                basin_sizes.append(basinsize)
    basin_sizes.sort()
    print(basin_sizes)
    return basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]


def main():
    """main function docstring"""
    cavern = getinput("input/example.txt")
    print(traversegrid(cavern))
    print(get_lowpoints(cavern))
    print(part2(cavern))


if __name__ == "__main__":
    main()
