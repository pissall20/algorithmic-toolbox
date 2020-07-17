
def gcd_euclid(a, b):
    if b == 0:
        return a
    rem = a % b
    return gcd_euclid(b, rem)


def lcm(n1, n2):
    ans = (n1 * n2)//gcd_euclid(n1, n2)
    return ans


if __name__ == '__main__':
    # input = sys.stdin.read()
    a, b = map(int, input().split(" "))
    print(lcm(a, b))
