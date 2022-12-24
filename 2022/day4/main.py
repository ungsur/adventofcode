with open('input/input1.txt', encoding='UTF-8') as fh:
    A = []
    for line in fh:
        A.append(line.strip())
    count = 0
    for line in A:
        thestack = []
        first, second = line.split(',')
        fi, fo = first.split('-')
        si, so = second.split('-')
        fi, fo, si, so = int(fi), int(fo), int(si), int(so)
        thestack.append([fi, fo])
        thestack.append([si, so])
        # print(thestack, "A stack")
        Alen, Blen = fo - fi + 1, so - si + 1
        if fi <= si:
            if Blen + fi <= fo:
                count += 1
                # print(thestack, count)
        elif si < fi:
            if Alen + si <= so:
                count += 1
                # print(thestack, count)
            else:
                print(thestack, "badstack")
    print(count)
