# 📅 Day 04 – Masking, Normalization & Matrix Tricks

**Mode:** Easy  
**Questions Completed:** Q15–Q20 / 20 (Easy Mode)  
**Time Spent:** ~1–1.5 hours  
**Status:** Foundations Conquered 🏆  

---

## ✅ Questions Solved

**Q15.** Count elements greater than 50 in a random integer array  
**Q16.** Generate a boolean mask for elements divisible by 3  
**Q17.** Extract all negative values from an array  
**Q18.** Create a 4×4 checkerboard matrix of 0s and 1s  
**Q19.** Normalize a 1D array to range [0, 1] using vectorized operations  
**Q20.** Swap the first and last rows of a 5×5 matrix  

---

## 🛠 Concepts Reinforced

### 🔹 Boolean Masking Mastery
- Constructing masks with modular arithmetic (`arr % 3 == 0`)  
- Extracting subsets directly via masks  
- Counting via `np.count_nonzero()`  

### 🔹 Conditional Extraction
- Negative value filtering with `arr[arr < 0]`  
- Purely vectorized selection — no loops  

### 🔹 Structured Matrix Design
- Checkerboard creation using slicing and modular patterns  
- Leveraging `np.indices()` for elegant alternating structures  

### 🔹 Normalization & Scaling
- Min-max normalization: `(arr - arr.min()) / (arr.max() - arr.min())`  
- Ensuring numerical stability with vectorized operations  

### 🔹 Row Manipulation
- Row swapping via slicing and temporary storage  
- Reinforcing shape discipline in transformations  

---

## ⚙️ Performance Notes

- All problems solved without explicit loops  
- Boolean masks proved to be the most versatile tool  
- Normalization pipeline fully vectorized — no manual iteration  
- Matrix tricks (checkerboard, row swaps) highlighted the power of slicing  

Average time per problem: ~15 minutes  

---

## 🧩 Key Technical Observations

- Boolean masks are the backbone of conditional logic in NumPy  
- Normalization is a one-liner when you think in arrays, not elements  
- Checkerboard patterns reveal how indexing can encode logic visually  
- Row operations emphasize the importance of axis awareness  

---

## 🧠 Micro-Learning Insight

Day 04 marks the **completion of Easy Mode**.  
The journey so far has shown that:

- Loops are obsolete when masks exist  
- Structural manipulation is about **axes, not elements**  
- Normalization and scaling are natural extensions of vectorization  

This is the turning point — NumPy starts feeling like a language of shapes and logic.

---

## 📊 Difficulty Reflection

Easy Mode complete ✅  
The problems were approachable but layered with insights:  
- Masking logic  
- Normalization pipelines  
- Structural transformations  

The foundation is now solid for tackling **Moderate Mode**.

---

## 🔥 Streak Tracker

Day 04 Complete  
Quest Progress: **20 / 90** (22.2%)  

Level 1 (Easy) — **DOMINATED** 🟢  
Next stop: Level 2 — Core Manipulation ⚡