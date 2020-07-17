# Uses python3

import sys


def is_better(num, max_num):
    if int(str(num)+str(max_num)) > int(str(max_num)+str(num)):
        return True
    return False


def largest_number(numbers):
    # write your code here
    res = []
    while numbers:
        max_num = 0
        for num in numbers:
            if is_better(num, max_num):
                max_num = num
        res.append(max_num)
        numbers.remove(max_num)
    return "".join((str(x) for x in res))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    a = [int(x) for x in a]
    print(largest_number(a))

