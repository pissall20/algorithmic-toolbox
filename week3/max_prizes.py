# Uses python3
import sys


def optimal_summands(n):
    summands = []

    for i in range(1, n+1):
        n -= i

        if n <= i:
            summands.append(i+n)
            break
        elif n == 0:
            summands.append(i)
            break
        else:
            summands.append(i)

    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
