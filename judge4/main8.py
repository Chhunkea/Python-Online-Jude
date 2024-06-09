# TODO: The Euclidean algorithm(2)

def euclidean_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

x, y = 84, 60
gcd = euclidean_gcd(x, y)
print(f"{x} and {y}: {gcd}")
