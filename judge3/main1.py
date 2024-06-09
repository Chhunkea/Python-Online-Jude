# TODO: Factorial

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        result = 1
        for i in range(2, N + 1):
            result *= i
        return result

N = 6
print(factorial(N))