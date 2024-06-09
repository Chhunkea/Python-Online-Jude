# TODO: Print from 0 to n using a recursive call

def from_zero_to_n(n):
    if n == 0:
        print(n)
    else:
        from_zero_to_n(n - 1)
        print(n)

n = 20
from_zero_to_n(n)