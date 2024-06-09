# TODO: Fibonacci numbers

def fibonacci_rabbits(N):
    # Initialize the list to store the number of pairs for each month
    pairs = [0] * (N + 1)

    # The first two months have 1 pair of rabbits
    pairs[1] = pairs[2] = 1

    # The number of pairs for each month starting from the third month
    for month in range(3, N + 1):
        pairs[month] = pairs[month - 1] + pairs[month - 2]
    return pairs[N]

N = 20
print(fibonacci_rabbits(N))