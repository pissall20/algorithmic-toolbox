import random
import time

def max_pairwise_product(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] * arr[j] > res and i != j:
                res = arr[i] * arr[j]
    return res


def max_pairwise_product_2(arr):
    max_index1, max_index2 = -1, -1
    for i in range(len(arr)):
        if max_index1 == -1 or arr[i] > arr[max_index1]:
            max_index1 = i

    for i in range(len(arr)):
        if (max_index2 == -1 or arr[i] > arr[max_index2]) and max_index1 != i:
            max_index2 = i
    return arr[max_index1] * arr[max_index2]


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().rstrip().split(" ")))
    # array = random.sample(range(1, 10001), 10000)
    # t0 = time.time()
    # result1 = max_pairwise_product(array)
    # t1 = time.time()
    # print("Time taken: {0}".format(t1-t0))
    # print("Result: {}".format(result1))

    t0 = time.time()
    result2 = max_pairwise_product_2(array)
    t1 = time.time()
    # print("Time taken: {0}".format(t1 - t0))
    print(result2)
    # print("Result: {}".format(result2))
    # if result1 != result2:
    #     print("Problem")

