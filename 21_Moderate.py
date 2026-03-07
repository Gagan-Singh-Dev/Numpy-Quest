# Question: Subtract the mean of each row from a 2D array’s elements.

import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

result = x - x.mean(axis = 1, keepdims = True, dtype = int)
print(f"Original Array: \n{x}")
print(f"Result Array: \n{result}")