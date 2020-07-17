import sys


def compute_min_refills(distance, tank, stop_lst):
    # write your code here
    n_ref, curr_ref = 0, 0
    n = len(stop_lst)

    stop_lst = [0] + stop_lst + [distance]
    while curr_ref < n:
        last_ref = curr_ref

        while (curr_ref < n) and (stop_lst[curr_ref+1] - stop_lst[last_ref] <= tank):
            curr_ref += 1

        if curr_ref == last_ref:
            return -1
        if curr_ref <= n:
            n_ref += 1
    return n_ref


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))


# 950
# 400
# 4
# 200 375 550 750

# 10
# 3
# 4
# 1 2 5 9