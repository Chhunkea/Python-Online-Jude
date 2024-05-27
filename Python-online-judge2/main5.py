#TODO:

def perm(n, r):
    result = 1
    for i in range(n - r + 1, n + 1):
        result *= i
    return result

n, r = 77, 11
print(perm(n, r))