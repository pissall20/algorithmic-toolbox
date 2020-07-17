# Uses python3
import sys
import random

"""
def partition(arr, pivot):
    less, equal, more = list(), list(), list()
    for elem in arr:
        if elem < pivot:
            less.append(elem)
        if elem == pivot:
            equal.append(elem)
        if elem > pivot:
            more.append(elem)
    return less, equal, more


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less, equal, more = partition(arr, pivot)
    return quick_sort(less) + equal + quick_sort(more)
"""

def partition3(arr, l, r):
    pivot = arr[l]
    j, t = l, r
    i = j
    while i <= t:
        if arr[i] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        elif arr[i] > pivot:
            arr[t], arr[i] = arr[i], arr[t]
            t -= 1
            i -= 1
        i += 1
    return j, t

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=' ')
