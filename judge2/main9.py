# TODO: Ackerman function

def ackermann(n, m, c=[0]):
    c[0] += 1
    return (m + 1) if n == 0 else (
           ackermann(n - 1, 1, c) if m == 0 else 
           ackermann(n - 1, ackermann(n, m - 1, c), c)
           )

n, m = 3, 3
call_counter = [0]
result = ackermann(n, m, call_counter)

print(result)
print(call_counter[0])
