
def main(num):
    # number of operations required to get 1, 2, ...., n
    num_operations = [0, 0] + [float("inf")] * (num-1)
    for i in range(2, num+1):
        temp1, temp2, temp3 = [float('inf')] * 3
        temp1 = num_operations[i-1] + 1
        if i % 2 == 0:
            temp2 = num_operations[i // 2] + 1
        if i % 3 == 0:
            temp3 = num_operations[i // 3] + 1
        # minimum out of 3 operations
        min_ops = min(temp1, temp2, temp3)
        num_operations[i] = min_ops

    # print number of operations for given num
    print(num_operations[num])

    # start backtracking the numbers leading to given num
    nums = [num]
    while num != 1:
        if num % 3 == 0 and num_operations[num]-1 == num_operations[num//3]:
            nums += [num//3]
            num = num // 3
        elif num % 2 == 0 and num_operations[num]-1 == num_operations[num//2]:
            nums += [num//2]
            num = num // 2
        else:
            nums += [num-1]
            num -= 1
    print(' '.join([str(i) for i in nums][::-1]))


if __name__ == "__main__":
    n = int(input())

    main(n)
