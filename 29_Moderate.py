# Question: Replace NaN values in a dataset with the respective column mean.

import numpy as np

x = np.array([[1, 2, np.nan],
              [4, np.nan, 6],
              [7, 8, 9]])

print(f"Original Array: \n{x}")

# Compute column means ignoring NaNs
col_means = np.nanmean(x, axis=0)

# Find indices where NaNs occur
inds = np.where(np.isnan(x))

# Replace NaNs with the corresponding column mean
x[inds] = np.take(col_means, inds[1])

print(f"Result Array: \n{x}")