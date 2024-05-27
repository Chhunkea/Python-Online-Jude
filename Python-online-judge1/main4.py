
def prime(n):
    if n <= 1:
        return False
    sqrtnum = int(n ** 0.5)
    for i in range(2, sqrtnum + 1):
        if n % i == 0:
            return False
    return True

lst = []
for i in range(4294967295, 2147483647, -1):
    if prime(i):
        lst.append(i)
    if len(lst) == 5:
        break

print(*lst)