# 🔹 What is a List in Python?
# A list is a built-in Python data structure used to store multiple items in a single variable.
# It is ordered, mutable (can change), and can contain any data type — including other lists!

# 📦 Analogy:
# Think of a list like a shopping basket:
# You can add/remove/change items
# You can put different types of items (milk, eggs, a note)
# Order matters — the first item is at the top

# 🔹 Syntax
# my_list = [1, 2, 3, 4]
# You define a list using square brackets [], and elements are separated by commas.

# 🔹 Key Properties
# Property	Meaning
# Ordered	Items have a defined order (index starts at 0)
# Mutable	You can change elements (add/remove/update)
# Heterogeneous	Can store different data types
# Dynamic	Size can grow or shrink dynamically

# 🔹 Accessing Elements
# my_list = ["apple", "banana", "cherry"]
# print(my_list[0])    # Output: apple
# print(my_list[-1])   # Output: cherry (last item)
# Use indexing to access elements

# Negative index starts from the end

# 🔹 Common Operations
# ✅ 1. Add Elements
# a = [1, 2, 3]

# a.append(4)          # ➤ Adds 4 at the end
# a.insert(1, 100)     # ➤ Adds 100 at index 1
# a.extend([5, 6])     # ➤ Adds multiple elements at the end
# ✅ 2. Remove Elements
# a.remove(2)          # ➤ Removes first occurrence of 2
# a.pop()              # ➤ Removes last element
# a.pop(0)             # ➤ Removes element at index 0
# del a[1]             # ➤ Deletes element at index 1
# ✅ 3. Update Elements
# a[0] = 999           # ➤ Changes first element to 999
# 🔹 Loop Through a List
# for fruit in ["apple", "banana", "cherry"]:
#     print(fruit)
# 🔹 List Slicing
# nums = [10, 20, 30, 40, 50]
# print(nums[1:4])     # ➤ [20, 30, 40]
# print(nums[:3])      # ➤ [10, 20, 30]
# print(nums[::-1])    # ➤ Reverses the list
# 🔹 Other Useful List Functions
# a = [1, 2, 3]

# len(a)        # ➤ Number of elements
# sum(a)        # ➤ Sum of all numbers
# min(a)        # ➤ Smallest
# max(a)        # ➤ Largest
# a.index(2)    # ➤ First index of 2
# a.count(3)    # ➤ Count of 3
# 🔹 Nested Lists (List of Lists)
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(matrix[1][2])   # ➤ Output: 6
# 🔹 Mutability Example
# a = [1, 2, 3]
# print(id(a))    # e.g., 139840198870912

# a.append(4)
# print(id(a))    # Same ID → list is mutable
# 🧠 When to Use Lists?
# When you need ordered data

# When the data might change

# For iterating, modifying, slicing items easily

# ❗ Warning: Copying Lists
# a = [1, 2, 3]
# b = a           # b and a refer to the same list

# b[0] = 100
# print(a)        # ➤ [100, 2, 3] — a is also changed

# # To create a copy
# c = a[:]        # or use c = list(a)
# ✅ Summary
# Feature	Supports
# Indexed	✅ Yes
# Mutable	✅ Yes
# Duplicate values	✅ Yes
# Mixed types	✅ Yes
# Nesting	✅ Yes


# 🔹 6. List Comprehension
# A short way to create lists using loops and conditions.

# # Example: Square of numbers
# squares = [x**2 for x in range(5)]
# print(squares)  # Output: [0, 1, 4, 9, 16]

# # Example: Filter even numbers
# even = [x for x in range(10) if x % 2 == 0]
# print(even)     # Output: [0, 2, 4, 6, 8]
# 🔹 7. Important List Methods
# Method	Description
# append()	Add item to end
# insert()	Insert at specific index
# extend()	Add multiple items
# remove()	Remove by value
# pop()	Remove by index
# clear()	Empty list
# sort()	Sort list
# Type	Syntax	Result
# Alphabetical	list.sort()	A → Z
# Alphabetical ↓	list.sort(reverse=True)	Z → A
# Numerical	list.sort()	Small → Big                                sort trick       💥💥💥❤🎉🎉🎉👌👌✅✅✅
# Numerical ↓	list.sort(reverse=True)	Big → Small
# Ignore case	list.sort(key=str.lower)	Case-insensitive sort
# Custom	list.sort(key=some_function)	Based on custom rule (e.g. len)
# reverse()	Reverse list order
# index()	Return index of first occurrence
# count()	Count how many times an item appears
# copy()	Shallow copy of list