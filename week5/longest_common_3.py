

def lcs3(a, b, c):
    matrix = [[[0 for i in range(len(c)+1)] for j in range(len(b)+1)] for k in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for k in range(len(c)+1):
                if i == 0 or j == 0 or k == 0:
                    matrix[i][j][k] = 0
                elif a[i-1] == b[j-1] == c[k-1]:
                    matrix[i][j][k] = 1 + matrix[i-1][j-1][k-1]
                else:
                    matrix[i][j][k] = max(matrix[i-1][j][k], matrix[i][j-1][k], matrix[i][j][k-1])
    return matrix[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    strings = []
    for c_in in range(3):
        n = int(input())
        data = list(map(int, input().split()))
        strings.append(data)

    print(lcs3(*strings))
