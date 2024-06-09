# TODO: Collatz sequence(2)

def collatz_operations(N):
    count = 0
    while N != 1:
        if N % 2 == 0:
            N //= 2
        else:
            N = 3 * N + 1
        count += 1
    return count - 2

N = 10
print(collatz_operations(N)) 
