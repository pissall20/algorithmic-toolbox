import sys


def lcs2(input1, input2):
    len_s1, len_s2 = len(input1), len(input2)

    matrix = [[0 for i in range(len_s2 + 1)] for i in range(len_s1 + 1)]

    maxim = 0

    for i in range(1, len_s1+1):
        for j in range(1, len_s2+1):
            if input1[i-1] == input2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            elif input1[i-1] != input2[j-1]:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

            if matrix[i][j] > maxim:
                maxim = matrix[i][j]

    return maxim


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

