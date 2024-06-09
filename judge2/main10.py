# TODO: Operation process of Factorial

def factorial_process(N):
    if N == 1:
        return "1"
    else:
        factorial = "1"
        for i in range(2, N + 1):
            factorial += f"*{i}"
        return factorial

N = int(input())
print(factorial_process(N))
