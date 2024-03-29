# def solve(n):
#     cnt = 0
#     sqrt = int(n ** 0.5)
#     for i in range(1, sqrt + 1):
#         if n % i == 0:
#             cnt += 2
#     if sqrt * sqrt == n:
#         cnt -= 1
#     return cnt
# N = int(input())
# print(solve(N))

def sum_of_divisors(N):
    div_sum = 0
    i = 1
    while i * i <= N:
        if N % i == 0:
            div_sum += i
            if i != N // i:
                div_sum += N // i
        i += 1
    return div_sum

N = 1234567890

import time 
start = time.time()
print(sum_of_divisors(N))
end = time.time()
print(f'solve() elapsed time : {end - start}')