

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
        a, b = b, (a + b)
    return b % m


def sum_of_squares(n):
    square_sum = fib_huge(n, 10) * fib_huge(n + 1, 10)
    return square_sum % 10


num = int(input())
print(sum_of_squares(num))
