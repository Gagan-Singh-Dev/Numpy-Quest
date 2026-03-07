# Question: Compute row-wise and column-wise sums without explicit loops.

import numpy as np

x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

row_sum = x.sum(axis=1, keepdims=True)
column_sum = x.sum(axis=0, keepdims=True)

print(f"Original Matrix: \n{x}")
print(f"Row-Wise Sum: \n{row_sum}")
print(f"Column-Wise Sum: \n{column_sum}")