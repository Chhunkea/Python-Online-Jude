#TODO: Find divisors of number 'n'
n = 211224

divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

for divisor in divisors:
    print(divisor)