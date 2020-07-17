
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(1, n):
        a, b = b, a+b
    return b


num = int(input())
print(fibonacci(num))
