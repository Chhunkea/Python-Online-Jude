
import random

SEED, MIN, MAX, N = map(int, input().split()) # Use map function to for int
random.seed(SEED)# Set the random seed
S = random.sample(range(MIN, MAX), N) # Generate the list of random integers

min_value = min(S) # print the smallest value
min_index = S.index(min_value) # print the indexing of the element with the smallest value

print(min_value, min_index)
