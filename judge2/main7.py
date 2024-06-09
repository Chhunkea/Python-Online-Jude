# TODO: Collatz sequence

def collatz_length(n):
    length = 1
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        length += 1
    return length

def find_longest_collatz(N, M):
    return max((collatz_length(i), i) for i in range(N, M + 1))[::-1]

N, M = 123, 321
number, length = find_longest_collatz(N, M)

print(number)
print(length)