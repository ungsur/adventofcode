def get_file(inputfile):
    with open(inputfile) as f:
        inputlist = f.readlines()
    return inputlist  

def get_position(inputlist):
    h, d, a = 0, 0, 0
    for pos in inputlist:
        dir, mag = pos.split()
        if dir == 'forward':
            h += int(mag)
            d += a * int(mag) 
        elif dir == 'up':
            a -= int(mag)
        elif dir == 'down':
            a += int(mag)
    print(h, d, a)
    return h*d

def main():
    inputfile = './input/example.txt'
    print(get_position(get_file(inputfile)))

if __name__ == '__main__':
    main()