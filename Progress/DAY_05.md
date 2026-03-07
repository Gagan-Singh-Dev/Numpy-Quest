# 📅 Day 05 – Row Operations, Diagonal Tricks & Core Manipulation

**Mode:** Moderate  
**Questions Completed:** Q21–Q25 / 25 (Moderate Mode)  
**Time Spent:** ~0.5-1 hours  
**Status:** First Steps into Moderate ⚡  

---

## ✅ Questions Solved

**Q21.** Subtract the mean of each row from a 2D array’s elements  
**Q22.** Replace diagonal elements of a square matrix with zeros  
**Q23.** Compute row-wise and column-wise sums without explicit loops  
**Q24.** Create a 10×10 matrix of random floats and find the top 5 largest values  
**Q25.** Find common elements between two arrays using vectorized operations  

---

## 🛠 Concepts Reinforced

### 🔹 Row-wise Mean Adjustment
- Applied broadcasting to subtract row means directly  
- Verified shape alignment for subtraction  

### 🔹 Diagonal Manipulation
- Used indexing to target diagonal positions  
- Replaced values efficiently without loops  

### 🔹 Aggregation Across Axes
- Leveraged `sum(axis=0)` and `sum(axis=1)`  
- Practiced axis awareness for row vs column operations  

### 🔹 Random Float Generation & Selection
- Generated controlled random floats in a matrix  
- Extracted top values using sorting and slicing  

### 🔹 Common Element Detection
- Utilized set-like operations (`np.intersect1d`)  
- Achieved clean vectorized comparison  

---

## ⚙️ Performance Notes

- All problems solved loop-free  
- Broadcasting proved essential for row operations  
- Axis-based aggregation reinforced structural clarity  
- Sorting and intersection methods were direct and efficient  

Average time per problem: ~15–20 minutes  

---

## 🧩 Key Technical Observations

- Row-wise mean subtraction highlights the power of broadcasting  
- Diagonal replacement requires precise indexing discipline  
- Axis-based sums are intuitive once shape orientation is clear  
- Random float generation + top-k extraction is a practical data task  
- Intersection operations simplify comparisons between arrays  

---

## 🧠 Micro-Learning Insight

Moderate Mode begins with **structural manipulation and aggregation**.  
The transition feels natural:  
- From element-level thinking → to row/column-level reasoning  
- From basic masks → to more complex indexing and set operations  

This stage emphasizes **clarity in axes and broadcasting logic**.

---

## 📊 Difficulty Reflection

Moderate Mode — first taste ✅  
Problems were approachable but demanded sharper axis awareness and indexing precision.  
The focus shifted from *foundations* to *core manipulation*.  

---

## 🔥 Streak Tracker

Day 05 Complete  
Quest Progress: **25 / 90** (27.8%)  

Level 2 (Moderate) — **Initiated** 🟡  
Momentum strong, deeper manipulation unlocked 🚀