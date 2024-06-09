# TODO: Sorting Characters

N = 6
characters = "AaBbCc"

# Sort and print uppercase letters in ascending order
upper_sorted = ''.join(sorted(filter(str.isupper, characters)))

# Sort and print lowercase letters in descending order
lower_sorted = ''.join(sorted(filter(str.islower, characters), reverse=True))

# Print both lines with a space between them
print(upper_sorted + '  ' + lower_sorted)
