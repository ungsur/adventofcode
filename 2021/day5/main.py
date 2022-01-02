def process_input(input):
    pointslist = []
    with open(input) as f:
        linesarr = f.readlines()
    for line in linesarr:
        p1, p2 = line.strip('\n').split('->')
        x1, y1 = list(map(int, p1.strip('\n').split(',')))
        x2, y2 = list(map(int, p2.strip('\n').split(',')))
        pointslist.append([[x1, y1], [x2, y2]])
    return pointslist


def drawline(p1, p2):
    pointslist = [p1]
    p3 = []
    print(p1, p2, p3)
    while p3 != p2:
        if p1[0] == p2[0] and p1[1] < p2[1]:
            p3 = [p1[0], p1[1] + 1]
        if p1[0] == p2[0] and p1[1] > p2[1]:
            p3 = [p1[0], p1[1]-1]
        if p1[0] > p2[0] and p1[1] == p2[1]:
            p3 = [p1[0]-1, p1[1]]
        if p1[0] < p2[0] and p1[1] == p2[1]:
            p3 = [p1[0]+1, p1[1]]
        pointslist.append(p3)
        p1 = p3
    return pointslist


def drawdiag(p1, p2):
    pointslist = [p1]
    p3 = []
    while p3 != p2:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            p3 = [p1[0]+1, p1[1]+1]
        if p1[0] < p2[0] and p1[1] > p2[1]:
            p3 = [p1[0]+1, p1[1]-1]
        if p1[0] > p2[0] and p1[1] < p2[1]:
            p3 = [p1[0]-1, p1[1]+1]
        if p1[0] > p2[0] and p1[1] > p2[1]:
            p3 = [p1[0]-1, p1[1]-1]
        pointslist.append(p3)
        p1 = p3
    return pointslist


def populategrid(pointslist: list):
    grid = {}
    linelist = []
    for point in pointslist:
        p1, p2 = point[0], point[1]
        if p1[1] != p2[1] and p1[0] != p2[0]:
            linelist += drawdiag(p1, p2)
        if p1[0] == p2[0]:
            linelist += drawline(p1, p2)
        if p1[1] == p2[1]:
            linelist += drawline(p1, p2)
    for item in linelist:
        point = str(item)
        if grid.get(point):
            grid[point] += 1
        else:
            grid[point] = 1
    print(len([k for k, v in grid.items() if v > 1]))
    # cprint(grid)


def main():
    input = './input/input.txt'
    points = process_input(input)
    populategrid(points)
    # print(drawline([0,5],[4,5]))


if __name__ == '__main__':
    main()
