#TODO: Sort numbers in ascending order
def sort_numbers():
    n = 10
    numbers = []

    for i in range(n):
        numbers.append(i + 1)

    for num in numbers:
        print(f"Number of operations {num}")

sort_numbers()