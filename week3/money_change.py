def get_change(m):
    coins = 0
    while m > 0:
        if m >= 10:
            m -= 10
        elif m >= 5:
            m -= 5
        else:
            m -= 1
        coins += 1
    return coins


def get_change_fast(m):
    return int(int(m / 10) + ((m % 10) / 5) + (m % 5))


if __name__ == '__main__':
    money = int(input())

    # print(get_change(money))

    print(get_change_fast(money))

