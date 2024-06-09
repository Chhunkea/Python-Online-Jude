# TODO: Triple Fibonacci sequence

def triple_fibonacci(N):
    if N <= 3:
        return N
    a, b, c = 1, 2, 3
    
    for _ in range(4, N + 1):
        a, b, c = b, c, (a + b + c) % (2**32 - 1)
    return c

N = 100000
print(triple_fibonacci(N))
