# Question: Compute mean, median, and standard deviation of a random array of size 50.

import numpy as np

x = np.random.randint(0, 11, 50, dtype="int")
print(f"Array : {x}")
print(f"Mean: {np.mean(x)}.")
print(f"Median: {np.median(x)}.")
print(f"Standard Deviation: {np.std(x)}.")

# If you want the sample standard deviation (instead of population)
# With Degree of Freedom
print(f"Sample Standard Deviation: {np.std(x, ddof=1)}.")

# Standard deviation is just the square root of variance
print(f"Standard Deviation (via varience): {np.sqrt(np.var(x))}.")