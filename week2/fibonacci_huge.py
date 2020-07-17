

def pisano_period(n):
    prev, curr = 0, 1
    for i in range(n*n):
        prev, curr = curr, (prev+curr) % n
        if prev == 0 and curr == 1:
            return i + 1
    return 1


def fib_huge(n, m):
    pisano_value = pisano_period(m)
    ans = n % pisano_value

    if ans <= 1:
        return ans
    a, b = 0, 1
    for i in range(ans-1):
        a, b = b, a + b
    return b % m


num, exp = list(map(int, input().split(" ")))
print(fib_huge(num, exp))
