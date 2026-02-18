
---

# 📚 **Day 3 — Theoretical Concepts**

### 1️⃣ Pandas Basics

* **Series**: 1D labeled array, holds data of any type.
* **DataFrame**: 2D labeled structure, like a table or spreadsheet.
* **Indexing**:

  * `.loc` → label-based indexing
  * `.iloc` → integer-based indexing
* **Adding/deleting columns**:

  * `df['new_col'] = ...`
  * `df.drop(columns=[...], inplace=True)`
* **Sorting**:

  * `sort_values()`
  * Single or multiple columns
* **Filtering**:

  * Boolean masks, conditional selection

---

### 2️⃣ Data Input/Output

* **CSV, Excel, JSON** handling:

  * `read_csv()`, `read_excel()`, `read_json()`
  * `to_csv()`, `to_excel()`
* **Handling large datasets**:

  * Reading in chunks
  * Specifying column types (`dtype`)
* **Index columns**:

  * Use one column as index for faster access

---

### 3️⃣ Data Cleaning

* **Missing values**:

  * Detect: `isnull()`, `notnull()`
  * Handle: `dropna()`, `fillna()`
* **Duplicates**:

  * Detect: `duplicated()`
  * Remove: `drop_duplicates()`
* **Data type conversions**:

  * `astype()` → convert between int, float, str, datetime
* **String operations**:

  * `.str.strip()`, `.str.lower()`, `.str.upper()`
  * `.str.replace()`, `.str.extract()`
* **Lambda functions in columns**:

  * Apply transformations efficiently

---

### 4️⃣ Exploratory Data Analysis (EDA) Basics

* **Descriptive statistics**:

  * `describe()`, `mean()`, `median()`, `std()`, `min()`, `max()`
* **Value counts & unique**:

  * `.value_counts()`, `.unique()`
* **Grouping & aggregation**:

  * `groupby()` + aggregation functions (`sum`, `mean`, `count`, `agg`)
* **Correlation**:

  * `df.corr()` → Pearson correlation between numerical columns
* **Sorting & ranking**:

  * `.sort_values()`, `.rank()`
* **Outlier detection**:

  * Using IQR: `Q1`, `Q3`, `IQR = Q3 - Q1`
  * Identify points outside `[Q1-1.5*IQR, Q3+1.5*IQR]`
* **Pivot tables / Cross-tabulation**:

  * Summarize data by multiple dimensions
  * `pivot_table()`, `crosstab()`

---

### 5️⃣ Project-Oriented Concepts

* **Data cleaning workflow**:

  * Load → Inspect → Clean → Transform → Save
* **Data validation**:

  * Check consistency, missing values, types, duplicates
* **EDA workflow**:

  * Summarize numeric and categorical data
  * Detect anomalies/outliers
  * Compute correlations
  * Generate basic plots (later in visualization phase)

---

✅ In short, **Day 3 theory** covers:
`Pandas data structures → Indexing/slicing → I/O → Cleaning → Transformation → Grouping → Aggregation → Correlation → Outlier detection → Pivoting`

---

If you want, I can make a **Day 3 concept map**, visually linking **all Pandas and EDA theory** for easier memory retention.

Do you want me to do that?
