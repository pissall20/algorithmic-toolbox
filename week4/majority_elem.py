def get_majority_element(arr):
    count_dict = dict()
    for elem in arr:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    max_count = 0
    majority_element = 0
    for k, v in count_dict.items():
        if max_count < v:
            max_count = v
            majority_element = k
    if count_dict[majority_element] > len(arr)/2:
        return 1
    else:
        return 0

def majoirty_elem_fast(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
            if count > len(arr)/2:
                return 1
    return 0


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().strip().split()))
    print(get_majority_element(a))
