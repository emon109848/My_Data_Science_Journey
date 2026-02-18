
---

# 📌 NUMPY CORE CONCEPTS — DETAILED CHEAT SHEET

---

## 1️⃣ NumPy Arrays (`np.array()`)

* **Purpose:** Efficient, homogeneous N-dimensional arrays.
* **Advantages over Python lists:**

  * Faster computation (vectorized operations)
  * Less memory usage
  * Support for multi-dimensional arrays (`ndarray`)

```python
import numpy as np
a = np.array([1, 2, 3])         # 1D
b = np.array([[1, 2], [3, 4]])  # 2D
c = np.array([[[1],[2]], [[3],[4]]])  # 3D
```

* Key properties: `.shape`, `.ndim`, `.size`, `.dtype`
* **Homogeneous data** → all elements same type

---

## 2️⃣ Shape & Dimensions

* `.shape` → tuple of dimensions
* `.ndim` → number of axes (rank)
* `.size` → total elements
* `.dtype` → data type
* **Axis concept:**

  * Axis 0 → rows (vertical)
  * Axis 1 → columns (horizontal)

```python
a = np.array([[1,2,3],[4,5,6]])
a.shape   # (2,3)
a.ndim    # 2
a.size    # 6
a.dtype   # int64 (system dependent)
```

---

## 3️⃣ Indexing & Slicing

* **1D Indexing & Slicing:**

```python
a = np.array([10,20,30,40])
a[0], a[1:3]   # 10, [20,30]
```

* **2D Indexing:**

```python
b = np.array([[1,2],[3,4]])
b[0,1]         # 2
b[:,1]         # [2,4] → all rows, column 1
```

* **Multi-dimensional slicing:**

  * `arr[start:stop:step]` per axis

* **Boolean Indexing:**

```python
a[a > 20]  # [30, 40]
```

* **Fancy Indexing:**

  * Select elements by array of indices

```python
a[[0,2]]   # [10,30]
```

---

## 4️⃣ Broadcasting

* **What:** Automatically expands smaller arrays to match shapes for arithmetic operations
* **Rules:**

  1. Compare shapes from right
  2. Dimensions must be equal or one of them = 1
  3. Smaller array **stretched** (without copying data)

```python
a = np.array([1,2,3])
b = np.array([[10],[20]])
a + 5         # scalar broadcast → [6,7,8]
a + b         # row/column expansion
```

* **Why powerful:** Avoids explicit loops → fast, concise code

---

## 5️⃣ Reshaping

* `.reshape()` → change shape of array (returns **view** if possible)
* Use `-1` to auto-calculate missing dimension
* `.flatten()` → returns **copy**
* `.ravel()` → returns **view** (no extra memory)

```python
a = np.array([1,2,3,4,5,6])
a.reshape(2,3)   # [[1,2,3],[4,5,6]]
a.reshape(-1,2)  # [[1,2],[3,4],[5,6]]
a.flatten()       # [1,2,3,4,5,6] → copy
a.ravel()         # [1,2,3,4,5,6] → view
```

---

## 6️⃣ Random Module

* Generate arrays of random numbers:

| Function                             | Description                     |
| ------------------------------------ | ------------------------------- |
| `np.random.rand()`                   | Uniform [0,1), shape arguments  |
| `np.random.randn()`                  | Standard normal (mean=0, std=1) |
| `np.random.randint(low, high, size)` | Random integers                 |
| `np.random.seed()`                   | Fix seed for reproducibility    |

```python
np.random.seed(42)
np.random.rand(3)          # e.g., [0.3745, 0.9507, 0.7319]
np.random.randn(3)         # e.g., [0.4967, -0.1383, 0.6477]
np.random.randint(0,10,5)  # e.g., [6,3,7,4,6]
```

* **Seeding** ensures same random numbers across runs → important for reproducible experiments

---

# 🔹 Quick Tips

* Use **vectorized operations** for speed
* **Broadcasting** avoids loops
* `.ravel()` → view, `.flatten()` → copy
* Always **check shapes** before operations
* Use **seed** for reproducibility in experiments

---

# 🔥 Interview Questions (NumPy Core)

1. Difference between Python list and NumPy array?
2. How to check shape, ndim, size, dtype?
3. Explain axis concept.
4. How does broadcasting work? Give example.
5. Difference between flatten() and ravel()?
6. How to generate random arrays and fix seed?
7. Explain Boolean and fancy indexing.
8. Why are NumPy arrays faster than lists?

---

If you want, I can **do the next cheat sheet for “NumPy Linear Algebra & Performance”** covering:

* Dot, transpose, inverse
* Eigenvalues/eigenvectors
* Vectorization vs loops
* Gradient descent step
* Covariance, identity matrix

All with **examples + interview questions**.

Do you want me to prepare that next?
