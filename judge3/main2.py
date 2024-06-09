# TODO: Factorial (2)

def factorial_process(N):
    if N == 0 or N == 1:
        return f"{N}!=1"
    else:
        factorial = f"{N}!=("
        result = 1
        for i in range(1, N + 1):
            result *= i
            factorial += str(i)
            if i < N:
                factorial += "*"
        factorial += f")={result}"
        return factorial

N = 6
print(factorial_process(N))
