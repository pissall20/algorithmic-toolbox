# Uses python3
import sys


def binary_search_iter(arr, key):
    left, right = 0, len(arr)
    # write your code here
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == key:
            return mid
        else:
            if key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return -1


def binary_search_rec(arr, key, minim, maxim):
    if maxim >= minim:
        mid = (minim + maxim)//2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search_rec(arr, key, minim, mid-1)
        else:
            return binary_search_rec(arr, key, mid+1, maxim)
    else:
        return -1


if __name__ == '__main__':
    input_data = sys.stdin.read()
    data = list(map(int, input_data.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search_rec(a, x, 0, len(a)-1), end=' ')
