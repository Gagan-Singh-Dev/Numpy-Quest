# 🧠 NumPy Quest: 90 Problems + BOSS Challenge

Welcome, adventurer! ⚔️  
This is your ultimate NumPy gauntlet: 90 progressively challenging problems designed to sharpen your vectorization skills, followed by the **BOSS Level** to test everything you’ve learned.  

Think of this as **strength training for your numerical brain** 🧮💪. No copy-pasting, no shortcuts — just pure NumPy mastery.

---

## 🎮 Levels

The quest is divided into four escalating levels:

- 🟢 **Level 1 – Easy (Foundations)**  
- 🟡 **Level 2 – Moderate (Core Manipulation)**  
- 🔵 **Level 3 – Hard (Advanced Vectorization & Logic)**  
- 🔴 **Level 4 – Extreme (Optimization, Linear Algebra, Complex Transformations)**  

Each level builds on the last — your loops will disappear, your broadcasting will shine, and your arrays will obey your commands.

---

## 🟢 Level 1 – Easy (Foundations)

1. Create a NumPy array of integers from 10 to 49.  
2. Build a 3×3 matrix filled with zeros.  
3. Create a 5×5 identity matrix.  
4. Generate 20 evenly spaced numbers between 0 and 1.  
5. Fill a 4×4 matrix with random integers from 1 to 100.  
6. Reshape a 1D array of size 12 into a 3×4 matrix.  
7. Extract the third element from a 1D array.  
8. Replace all even numbers in an array with -1.  
9. Find the maximum and minimum values of an array efficiently.  
10. Compute mean, median, and standard deviation of a random array of size 50.  
11. Create a 6×6 matrix with sequential values from 0 to 35.  
12. Reverse a 1D array without using loops.  
13. Flatten a 2D array.  
14. Stack two 1D arrays vertically into a single matrix.  
15. Count elements greater than 50 in a random integer array.  
16. Generate a boolean mask for elements divisible by 3.  
17. Extract all negative values from an array.  
18. Create a 4×4 checkerboard matrix of 0s and 1s.  
19. Normalize a 1D array to range [0, 1] using vectorized operations.  
20. Swap the first and last rows of a 5×5 matrix.  

---

## 🟡 Level 2 – Moderate (Core Manipulation)

21. Subtract the mean of each row from a 2D array’s elements.  
22. Replace diagonal elements of a square matrix with zeros.  
23. Compute row-wise and column-wise sums without explicit loops.  
24. Create a 10×10 matrix of random floats and find the top 5 largest values.  
25. Find common elements between two arrays using vectorized operations.  
26. Perform element-wise multiplication of two compatible matrices.  
27. Compute the dot product of two 1D arrays efficiently.  
28. Standardize each column of a 100×5 dataset.  
29. Replace NaN values in a dataset with the respective column mean.  
30. Find indices of elements between 20 and 40 in a matrix.  
31. Create sliding windows of size 3 from a 1D array without loops.  
32. Sort each row of a 2D matrix independently.  
33. Compute cumulative sum along axis 1.  
34. Identify rows in a 2D array containing at least one zero.  
35. Remove duplicate rows from a 2D matrix.  
36. Reshape a 3D array (2×3×4) into (4×3×2).  
37. Broadcast a 1D array across rows of a 2D array and add them.  
38. Compute the correlation coefficient matrix of a 200×4 dataset.  
39. Compute pairwise Euclidean distances between rows of a 2D array.  
40. Identify the best-selling product from a sales dataset (days × products).  
41. Apply a custom function element-wise without explicit loops.  
42. Clip all values in an array between 10 and 100.  
43. Create a mask for prime numbers in an array.  
44. Rotate a matrix 90 degrees clockwise.  
45. Find the row with maximum sum in a 2D array.  

---

## 🔵 Level 3 – Hard (Advanced Vectorization & Logic)

46. Implement softmax row-wise for a 2D array without loops.  
47. Simulate a mini-batch gradient descent step using only NumPy.  
48. One-hot encode a label array of integers (0–9) efficiently.  
49. Compute moving average with window size k without loops.  
50. Implement column-wise min-max scaling.  
51. Detect local maxima in a time-series array without explicit loops.  
52. Vectorize computation of sigmoid and its derivative for a matrix.  
53. Find features with variance above a threshold in a 1000×20 dataset.  
54. Update k-means centroids using broadcasting.  
55. Zero out rows in a matrix where the sum exceeds a threshold.  
56. Construct a confusion matrix from predicted and actual labels.  
57. Compute rolling standard deviation along axis 0.  
58. Normalize each sample independently in a 3D tensor (samples × height × width).  
59. Compute cosine similarity between all row pairs of a matrix.  
60. Write a function to compute entropy of a probability distribution array.  
61. Detect duplicate columns in a matrix efficiently.  
62. Compute a covariance matrix without using np.cov.  
63. Generate polynomial features (degree ≤3) from a feature matrix.  
64. Compute daily returns from stock prices (days × companies).  
65. Simulate Monte Carlo random walk paths (1000 simulations).  
66. Find top k elements per row efficiently without full sorting.  
67. Replace outliers beyond 3 standard deviations.  
68. Implement batch normalization transformation on a dataset.  
69. Identify columns with multicollinearity (correlation > 0.9).  
70. Convert an image array (H×W×3) to grayscale using vectorized weights.  

---

## 🔴 Level 4 – Extreme (Optimization, Linear Algebra, Complex Transformations)

71. Solve a linear system Ax = b without explicit matrix inversion.  
72. Compute eigenvalues/eigenvectors of a covariance matrix and perform PCA.  
73. Implement logistic regression forward pass using only matrix multiplication.  
74. Build a fully vectorized neural network layer (linear + activation).  
75. Perform batched matrix multiplication for 3D tensors.  
76. Apply 2D convolution on an image using NumPy only (loops optional).  
77. Compute pairwise Mahalanobis distance between observations.  
78. Reduce dimensionality using SVD on a 1000×100 dataset.  
79. Efficiently compute Jacobian matrix for a softmax function.  
80. Implement cross-entropy loss for multi-class classification.  
81. Simulate Markov chain transitions for N steps using matrix exponentiation.  
82. Optimize large matrix multiplication for memory efficiency.  
83. Detect and correct singular matrices in a batch.  
84. Implement QR decomposition manually with NumPy.  
85. Compute Kronecker product between two matrices and apply to a vector.  
86. Generate a 3D Gaussian distribution grid.  
87. Implement vectorized backpropagation for a single-layer neural network.  
88. Compute a large-scale pairwise distance matrix (10,000×300) under memory constraints.  
89. Solve ridge regression using the normal equation.  
90. Apply vectorized feature extraction (mean, variance, skewness, kurtosis) across sliding windows for multi-dimensional time-series data.  

---

## 🏆 🔴 BOSS LEVEL – Ultimate NumPy Gauntlet

**Dataset (NumPy arrays only):**  

- `images` → `(1000, 64, 64, 3)` → RGB images  
- `stocks` → `(1000, 50)` → daily stock prices  
- `labels` → `(1000,)` → integers 0–9  
- `signals` → `(1000, 10, 10)` → extra sensor/time-series data  

**Objective:** Build a **fully vectorized NumPy pipeline** that does **feature extraction, transformation, reduction, prediction, and simulation**, all efficiently.  

---

### 🔹 Tasks

1. **Image Pipeline:**  
   - Convert RGB → grayscale using `[0.2989, 0.5870, 0.1140]` fully vectorized.  
   - Apply **3×3 convolution** (Sobel + Gaussian smoothing) on all images **without loops**.  
   - Flatten all images → `(1000, 64*64)`  

2. **Stock & Signal Processing:**  
   - Compute **daily returns** for `stocks`: `(P[t]-P[t-1])/P[t-1]`.  
   - Compute **rolling mean and std** (window=5) along axis 0, vectorized.  
   - Normalize stock features to `[0,1]`.  
   - Flatten `signals` and compute **mean, std, skewness, kurtosis** for each sample.  

3. **Feature Fusion:**  
   - Concatenate flattened images, stock features, and signal statistics → `X_final` `(1000, ?)`  
   - Apply **column-wise z-score normalization**  

4. **Dimensionality Reduction:**  
   - Compute **top 20 principal components** using eigen decomposition (NumPy only)  
   - Reduce `X_final` → `(1000, 20)`  

5. **Classification & Loss:**  
   - One-hot encode `labels` → `(1000,10)`  
   - Initialize `W` `(20,10)` and `b` `(10,)`  
   - Compute `Y_pred = softmax(X_final @ W + b)`  
   - Compute **cross-entropy loss**  

6. **Monte Carlo Simulation:**  
   - Simulate 1000 future stock scenarios: `X_scenario = X_final + np.random.normal(0, 0.01, X_final.shape)`  
   - Compute predicted label probabilities vectorized  
   - Identify most likely label class across all scenarios  

7. **Performance Challenge:**  
   - Entire pipeline must be **loop-free**  
   - Optimize memory with batch slicing if necessary  
   - Only **broadcasting, vectorization, and matrix algebra** allowed  

---

### 💥 Why this is Hardcore  

- Multiple **high-dimensional datasets** combined  
- Advanced **vectorized convolutions + statistics + PCA + Monte Carlo**  
- Tests **matrix algebra mastery, dimensional reasoning, and performance awareness**  
- Mimics **real-world pipelines** in finance, imaging, and ML  
- Only **NumPy allowed** — no pandas, no sklearn  

---

## 🔥 **Final Words:**  
Complete all 90 problems, survive the BOSS Level, and you will **truly think in NumPy**. Your arrays will obey your logic, your broadcasting will feel natural, and loops will be forever obsolete.  

Prepare your weapons — the matrix is waiting. ⚔️🧠
