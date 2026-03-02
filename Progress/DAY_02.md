# 📅 Day 02 – Indexing, Reshaping & Statistical Foundations

**Mode:** Easy   
**Questions Completed:** Q6–Q10 / 20 (Easy Mode)  
**Time Spent:** ~0.5–1 hours  
**Status:** Momentum Building ⚡  

---

## ✅ Questions Solved

**Q6.** Reshape a 1D array of size 12 into a 3×4 matrix  
**Q7.** Extract the third element from a 1D array  
**Q8.** Replace all even numbers in an array with -1  
**Q9.** Find maximum and minimum values efficiently  
**Q10.** Compute mean, median, and standard deviation of a random array (size 50)  

---

## 🛠 Concepts Reinforced

### 🔹 Reshaping & Dimensional Awareness
- `reshape()` mechanics and total element preservation rule  
- Understanding row-major memory layout  
- Shape compatibility reasoning  

### 🔹 Indexing & Element Access
- Zero-based indexing precision  
- Direct scalar extraction vs slicing  
- Avoiding off-by-one errors  

### 🔹 Boolean Masking (Core Skill)
- Vectorized condition filtering  
- Replacing values without loops  
- Broadcasting logical operations  

### 🔹 Efficient Aggregation
- `np.max()` / `np.min()`  
- `np.mean()`  
- `np.median()`  
- `np.std()`  
- Understanding axis-based computation  

---

## ⚙️ Performance Notes

- No explicit loops used  
- Fully vectorized replacements via boolean masks  
- Constant-time statistical operations  
- Clean memory transformations with zero data copying where possible  

Average time per problem: ~15–20 minutes  

---

## 🧩 Key Technical Observations

- Reshaping does not change data — only interpretation of memory layout  
- Boolean masks are fundamental to NumPy thinking  
- Statistical functions operate in optimized C under the hood — far faster than manual implementations  
- Dimensional clarity prevents most logical errors  

---

## 🧠 Micro-Learning Insight

Today marks the transition from *array creation* to *array manipulation*.  

The real power of NumPy appears when:
- You stop iterating  
- You start masking  
- You trust vectorized aggregation  

Thinking shifts from element-level to structure-level.

---

## 📊 Difficulty Reflection

Still in Easy Mode — but this layer introduces:

- Structural awareness (shapes matter)
- Conditional transformation logic
- Statistical summarization

These are foundational for upcoming broadcasting-heavy problems.

---

## 🔥 Streak Tracker

Day 02 Complete  
Quest Progress: **10 / 90** (11.1%)

Vectorization muscle memory is forming.  
Onward to deeper manipulation. 🚀
