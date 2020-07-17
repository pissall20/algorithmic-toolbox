

def get_change_fast(money, coins):
    min_num_coins = [0] + [float("inf")] * (money+1)
    for i in range(1, money+1):
        for coin in coins:
            if i >= coin:
                num_coins = min_num_coins[i - coin] + 1
                if num_coins < min_num_coins[i]:
                    min_num_coins[i] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    money = int(input())

    denominations = [1, 3, 4]

    # print(get_change(money))

    print(get_change_fast(money, denominations))

