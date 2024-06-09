#TODO: All prime numbers between two numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(m, n):
    for num in range(m, n + 1):
        # it's check if the value is prime or not
        if is_prime(num):
            print(num)

m, n = map(int, input().split())
print_primes(m, n)