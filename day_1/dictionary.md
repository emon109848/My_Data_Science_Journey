student = {
    "name": "Emon",
    "age": 25,
    "is_student": True
}

# 3️⃣ Creating Dictionaries
d = {}

person = {
    "name": "Emon",
    "age": 25
}

person = dict(name="Emon", age=25)


print(person.get("name"))

print(person.get("salary", 0))  # default value

# 7️⃣ Looping Through Dictionary

for key, value in person.items():
    print(key, value)

len(person)

# 🔟 Dictionary Comprehension (Advanced)

Like list comprehension but for dictionaries.


squares = {x: x*x for x in range(5)}
print(squares)


Output:


{0:0, 1:1, 2:4, 3:9, 4:16}


---

# 1️⃣1️⃣ Nested Dictionary

Dictionary inside dictionary.


students = {
    "student1": {
        "name": "Emon",
        "age": 25
    },
    "student2": {
        "name": "Rahim",
        "age": 22
    }
}


Access:


print(students["student1"]["name"])


---

# 1️⃣2️⃣ Dictionary with List


data = {
    "numbers": [1, 2, 3, 4],
    "names": ["Emon", "Rahim"]
}


Append:


data["numbers"].append(5)


---

# 1️⃣3️⃣ Copying Dictionary

⚠ Important concept


new_dict = person.copy()


Without copy:


new_dict = person  # Same memory!


---

# 1️⃣4️⃣ Sorting Dictionary

Sort by key:


sorted(person)


Sort by value:


sorted(person.items(), key=lambda x: x[1])


---

# 1️⃣5️⃣ Defaultdict (Advanced)

From collections:


from collections import defaultdict

freq = defaultdict(int)
freq["apple"] += 1


Automatically creates key with default value.

# 1️⃣8️⃣ Real World Example (Frequency Counter)


words = ["apple", "banana", "apple", "orange"]

freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


Output:


{'apple': 2, 'banana': 1, 'orange': 1}


🔥 Extremely important pattern.


# 2️⃣0️⃣ Dictionary Best Practices

✅ Use `.get()` to avoid errors
✅ Use meaningful keys
✅ Use dictionary comprehension when possible
✅ Use defaultdict for counters
✅ Avoid modifying dict while looping

---

# 🧠 Now Your Practice Tasks

1. Create a dictionary of 5 subjects and marks.
2. Find average marks.
3. Count frequency of letters in a word.
4. Create nested dictionary for 3 students.
5. Sort dictionary by values.

