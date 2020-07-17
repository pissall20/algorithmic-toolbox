

def sum_of(a, b):
    return a+b


if __name__ == "__main__":
    a1, b1 = map(int, input().rstrip().split(" "))
    print(sum_of(a1, b1))