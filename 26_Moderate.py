# Question: Perform element-wise multiplication of two compatible matrices.

import numpy as np

# Define two compatible matrices
x = np.array([[1, 2, 3],
              [4, 5, 6]])

y = np.array([[7, 8, 9],
              [10, 11, 12]])

result = np.multiply(x, y)

print(f"Array x: \n{x}")
print(f"Array y: \n{y}")
print(f"Result: \n{result}")