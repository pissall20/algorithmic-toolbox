
def gcd_euclid(a, b):
    if b == 0:
        return a
    rem = a % b
    return gcd_euclid(b, rem)




if __name__ == "__main__":
    a1, b1 = map(int, input().rstrip().split(" "))
    print(gcd_euclid(a1, b1))
