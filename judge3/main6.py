# TODO: A magical box and gold coins

def max_gold_coins(N):
    coins = [0] * (2 * N + 1)
    coins[1] = coins[2] = 1

    for i in range(1, N // 2 + 1):
        coins[2 * i] = coins[i]
        if 2 * i + 1 <= N:
            coins[2 * i + 1] = coins[i] + coins[i + 1]

    return max(coins)

N = 10
print(max_gold_coins(N))
