## 1️⃣ Two Ways to Sort

### 🔹 `sorted()`

* Works on any iterable (list, tuple, set, dict, string)
* Returns a **new list**
* Does NOT modify original

```python
new_list = sorted(data)
```

---

### 🔹 `.sort()`

* Works only on lists
* Modifies original list
* Returns `None`

```python
data.sort()
```

---

## 2️⃣ Syntax

```python
sorted(iterable, key=None, reverse=False)
```

### Parameters:

* `iterable` → data to sort
* `key` → custom sorting rule
* `reverse=True` → descending order

---

## 3️⃣ Default Behavior

* Numbers → ascending
* Strings → alphabetical (ASCII-based)
* Tuples → sorted by first element

---

## 4️⃣ Key Parameter (MOST IMPORTANT 🔥)

Used to define custom sorting logic.

Example:

```python
sorted(words, key=len)
```

Sort by length.

Using lambda:

```python
sorted(data, key=lambda x: x[1])
```

Sort by second element.

---

## 5️⃣ Sorting Dictionary

* `sorted(d)` → sorts keys
* Sort by value:

```python
sorted(d.items(), key=lambda x: x[1])
```

---

## 6️⃣ Multi-Level Sorting

```python
sorted(data, key=lambda x: (x[0], x[1]))
```

Sort by first value, then second.

---

## 7️⃣ Reverse Sorting

```python
sorted(data, reverse=True)
```

---

## 8️⃣ Stability (Important Interview Point)

Python sorting is **stable**.

If two elements are equal, their original order is preserved.

---

## 9️⃣ Time Complexity

| Case    | Complexity |
| ------- | ---------- |
| Average | O(n log n) |
| Worst   | O(n log n) |
| Best    | O(n)       |

Algorithm used: **Timsort**

---

## 🔟 Common Interview Differences

| sorted()               | sort()            |
| ---------------------- | ----------------- |
| Returns new list       | Modifies original |
| Works on all iterables | Only lists        |
| Functional style       | In-place          |

---

# 🧠 Mental Model

When using:

```python
sorted(data, key=function)
```

Python:

1. Applies function to each element
2. Uses returned value for comparison
3. Sorts elements
4. Returns new list

---

# 🔥 Must Remember

✔ Use `sorted()` when you need original data unchanged
✔ Use `key` for custom sorting
✔ Sorting is stable
✔ Time complexity is O(n log n)
..,                                                  h c