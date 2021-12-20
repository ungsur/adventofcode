def calculate_houses(input):
    revisit = []
    counted = []
    counter = 0
    x, y = 0, 0
    coordinate = (x,y)
    revisit.append(coordinate)
    for pos in input:
        if pos == '^':
            y += 1
        elif pos == 'v':
            y -= 1
        elif pos == '>':
            x += 1
        elif pos == '<':
            x -= 1
        coordinate = (x,y)
        revisit.append(coordinate)
        if coordinate in revisit and coordinate not in counted:
            counter += 1
            counted.append(coordinate)
    return counter

def robo_count(input):
    santainput = input[::2]
    roboinput = input[1::2]
    revisit = []
    counted = [(0, 0)]

    x, y, rx, ry = 0, 0, 0, 0
    coordinate = (x,y)
    revisit.append(coordinate)

    for pos in santainput:
        if pos == '^':
            y += 1
        elif pos == 'v':
            y -= 1
        elif pos == '>':
            x += 1
        elif pos == '<':
            x -= 1
        coordinate = (x,y)
        revisit.append(coordinate)
        if coordinate in revisit and coordinate not in counted:
            counted.append(coordinate)
    
    for pos in roboinput:
        if pos == '^':
            ry += 1
        elif pos == 'v':
            ry -= 1
        elif pos == '>':
            rx += 1
        elif pos == '<':
            rx -= 1
        coordinate = (rx,ry)
        revisit.append(coordinate)
        if coordinate in revisit and coordinate not in counted:
            counted.append(coordinate)
    print(counted)
    return len(counted)

def main():
    with open('./input/input.txt') as fh:
        input = fh.readline()
    #input = '^v^v^v^v^v'
    #print(calculate_houses(input))
    print(robo_count((input)))

if __name__=='__main__':
    main()