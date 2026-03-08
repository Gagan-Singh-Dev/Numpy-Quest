# Question: Standardize each column of a 100×5 dataset.

import numpy as np

x = np.random.rand(100, 5)
Result = (x - np.mean(x, axis=0)) / np.std(x, axis=0)

print(Result.shape)  # (100, 5)