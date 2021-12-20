def countfloors(inputstring):
    counter = 0
    position = 0
    for paren in inputstring:
        position += 1
        if paren == '(':
            counter += 1
        elif paren == ')':
            counter -= 1
        if counter == -1:
            return position
        
    return counter

def main():
    with open('./input/input.txt') as fh:
        input = fh.read()
    print(input)
    print(countfloors(input))

if __name__=='__main__':
    main()