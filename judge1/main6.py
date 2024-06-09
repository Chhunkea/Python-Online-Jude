# def small_prime_num(prime):
#     primes = [True] * prime
#     primes[0], primes[1] = False, False

#     for ind, val in enumerate(primes):
#         if val is True:
#             primes[ind*2::ind] = [False] * (((prime - 1)//ind) - 1)

#     return [ind for ind, val in enumerate(primes) if val is True]

# def find_kth_prime(a, b, k):
#     primes = small_prime_num(b + 1)
#     prime_sum = sum(primes[a-1:b+1])
#     if k > len(primes[a-1:b+1]):
#         return prime_sum, -1
#     else:
#         return prime_sum, primes[a-1:b+1][k-1]

# # Test the function
# a, b, k = map(int, input().split())
# prime_sum, kth_prime = find_kth_prime(a, b, k)
# print(prime_sum)
# print(kth_prime)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def small_prime_num(prime):
    primes = [num for num in range(prime) if is_prime(num)]
    return primes

def find_kth_prime(a, b, k):
    primes = small_prime_num(b + 1)
    prime_sum = sum(primes[a-1:b+1])
    if k > len(primes[a-1:b+1]):
        return prime_sum, -1
    else:
        return prime_sum, primes[a-1:b+1][k-1]

# Test the function
a, b, k = map(int, input().split())
prime_sum, kth_prime = find_kth_prime(a, b, k)
print(prime_sum)
print(kth_prime)
