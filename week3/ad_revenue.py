import sys


def max_dot_product(a, b):
    # write your code here
    a.sort()
    b.sort()
    res = sum((a[i]*b[i] for i in range(len(a))))
    return res


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

