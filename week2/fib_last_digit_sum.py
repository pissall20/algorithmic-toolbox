
def pisano_period(n):
    prev, curr = 0, 1
    for i in range(n*n):
        prev, curr = curr, (prev+curr) % n
        if prev == 0 and curr == 1:
            return i + 1
    return 1


def fibonacci_last_digit_sum(n):
    new_n = (n+2) % pisano_period(10)

    a, b = 0, 1
    for i in range(new_n-1):
        a, b = b % 10, (a+b) % 10

    if b == 0:
        return 9
    else:
        return (b % 10) - 1



num = int(input())
print(fibonacci_last_digit_sum(num))
