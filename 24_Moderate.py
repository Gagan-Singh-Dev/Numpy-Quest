# Question: Create a 10×10 matrix of random floats and find the top 5 largest values.

import numpy as np

x = np.random.rand(10, 10)

np.set_printoptions(precision=3, suppress=True)
flattened = x.flatten()
result = np.sort(flattened)[-5:]

print(x)
print(result)