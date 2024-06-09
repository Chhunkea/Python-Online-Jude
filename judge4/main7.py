# TODO: Find the number of triangles

def count_triangles(n):
    count = 0
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = n - a - b
            if c >= b and a + b > c:
                count += 1
    return count

n = 10
print("Number of triangles that can be created:", count_triangles(n))
