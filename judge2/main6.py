# TODO: Least common multiple of multiple numbers

import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

X = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = lcm_of_list(X)
print(result)
