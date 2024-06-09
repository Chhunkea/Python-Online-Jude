# TODO: Greatest common divisor of A and B

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int('1' * 3)  
B = int('1' * 6)  
print(gcd(A, B))
