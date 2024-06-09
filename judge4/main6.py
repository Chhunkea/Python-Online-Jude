# TODO: The Euclidean algorithm

def euclidean_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

x, y = 24, 64
print(euclidean_gcd(x, y))
