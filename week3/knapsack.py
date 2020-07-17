# Uses python3


def get_optimal_value(capacity, weight_list):
    value = 0.
    # write your code here
    props = sorted(weight_list, key=lambda x: x[0]/x[1], reverse=True)

    for val, weight in props:
        if capacity == 0:
            print(value)
        amount = min(capacity, weight)
        value += amount * val/weight
        capacity -= amount
    return value


if __name__ == "__main__":
    n, W = [int(i) for i in input().split()]
    lst = []

    if W == 0:
        print(0)
        quit()

    for _ in range(n):
        v, w = [int(i) for i in input().split()]
        if v == 0:
            continue
        lst.append((v, w))

    opt_value = get_optimal_value(W, lst)
    print("{:.4f}".format(opt_value))

# 3 50
# 60 20
# 100 50
# 120 30

# 1 10
# 500 30