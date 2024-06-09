#TODO: almost prime
def count_almost_primes(A, B):
    almost_primes_count = 0

    for num in range(max(2, A), B + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # if it prime number
        if is_prime:
            power = num * num
            while power <= B:
                if power >= A:
                    almost_primes_count += 1
                if power > B // num:
                    break
                power *= num

    return almost_primes_count

A, B = 1, 1000
print(count_almost_primes(A, B))
