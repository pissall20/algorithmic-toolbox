
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

def fibonacci_last_digit(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, (a+b) % 10
    return b


def fibonacci_partial_sum(n, m):
    if n == m:
        return fibonacci_last_digit(n % pisano_period(10))
    else:
        n_ans = fib_huge(n+1, 10) - 1
        m_ans = fib_huge(m+2, 10) - 1
        return (m_ans-n_ans) % 10


num, exp = list(map(int, input().split(" ")))
print(fibonacci_partial_sum(num, exp))
