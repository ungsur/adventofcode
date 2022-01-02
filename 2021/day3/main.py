def get_file(inputfile: str) -> list:
    with open(inputfile) as f:
        inputlist = []
        for line in f:
            inputlist.append(line.strip())
    return inputlist


def calculate_g(inputlist: list) -> int:
    listapp = []

    def _convert_bin(binstring):
        converted = []
        for num in binstring:
            if num == '0':
                converted.append('1')
            elif num == '1':
                converted.append('0')

        return int(''.join(converted), 2)

    for line in inputlist:
        listapp.append([x for x in line])
    listapp_t = list(zip(*listapp))
    finalbin = []
    for line in listapp_t:
        intline = map(int, line)
        num = sum(intline)/len(line)
        if num >= .5:
            finalbin.append('1')
        else:
            finalbin.append('0')
    finalval = int(''.join(finalbin), 2)
    comp = _convert_bin(finalbin)
    # print(finalval,comp)
    return finalval * comp


def calculate_scrubber(inputlist):
    o2 = inputlist.copy()
    o2_t = list(zip(*o2))
    co2 = inputlist.copy()

    def _bit_counter(arr, index):
        zeros, ones = 0, 0
        for line in arr:
            if line[index] == "0":
                zeros += 1
            if line[index] == '1':
                ones += 1
        return zeros, ones

    def recursive_search(arr, index):
        if len(arr) == 1:
            return arr[0]
        else:
            zeroes, ones = _bit_counter(arr, index)
            if ones >= zeroes:
                current_column = '1'
            else:
                current_column = '0'
            new_arr = []
            for item in arr:
                if item[index] == current_column:
                    new_arr.append(item)
            index += 1
        return recursive_search(new_arr, index)

    print(int(recursive_search(o2, 0), 2))

    return 282*3205


def main():
    inputfile = './input/example.txt'
    inputlist = get_file(inputfile)

    print(calculate_scrubber(inputlist))


if __name__ == '__main__':
    main()
