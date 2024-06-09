# TODO: Hailstone Sequence

def hailstone_sequence(N):
    max_number = N
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
        max_number = max(max_number, N)
    return max_number

N = 3
print(hailstone_sequence(N))
