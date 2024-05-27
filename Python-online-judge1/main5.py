n = int(input())
lst = [x for x in range(1, n + 1)]
result = list(map(lambda x : x ** 3, lst))
print(sum(result))