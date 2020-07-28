# Uses python3
import sys
import numpy as np


def optimal_weight(W, w):
    # write your code here
    matrix = np.zeros((len(w)+1, W+1), dtype=np.int)
    for i in range(1, len(w)+1):
        for j in range(1, W+1):
            if w[i-1] <= j:
                matrix[i][j] = max(matrix[i-1][j - w[i-1]] + w[i-1], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]
    return matrix[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
