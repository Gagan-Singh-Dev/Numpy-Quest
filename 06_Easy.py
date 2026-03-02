# Question: Reshape a 1D array of size 12 into a 3×4 matrix.

import numpy as np

x = np.zeros(12, dtype=int)
print(f"Original Array: {x}.")

result = np.reshape(x, (3, 4))
print(f"Reshaped Array: \n{result}")