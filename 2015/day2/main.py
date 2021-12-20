def calculate_paper(input):
    total = 0
    for line in input:
        lwh_string = line.strip().split('x')
        mapobj = map(int, lwh_string)
        l, w, h = mapobj
        subtotal = 2*l*w + 2*w*h + 2*h*l + min(l*w,w*h,h*l)
        print(l,w,h, subtotal)
        total += subtotal
    return total

def calculate_ribbon(input):
    total = 0
    for line in input:
        lwh_string = line.strip().split('x')
        mapobj = map(int, lwh_string)
        l, w, h = mapobj
        subtotal = min(2*(l+w), 2*(w+h), 2*(h+l)) + l*w*h
        print(l,w,h, subtotal)
        total += subtotal
    return total

def main():
    with open('./input/input.txt') as fh:
        input = fh.readlines()
    print(calculate_ribbon(input))

if __name__=='__main__':
    main()