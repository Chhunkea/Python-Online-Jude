# TODO: Print from n to 1 using recursive calls

def from_n_to_one(n):
    if n == 1:
        print(n)
    else:
        print(n, end=" ") 
        from_n_to_one(n - 1)

n = 10
from_n_to_one(n)
