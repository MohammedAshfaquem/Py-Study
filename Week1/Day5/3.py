# 📂 1. File Handling in Python – Reading & Writing Files
# 🔹 What is File Handling?
# File handling is how Python reads  and writes to files — like .txt, .csv, etc.
# This lets your program store and retrieve data permanently (unlike variables which are lost when the program ends).

# 📁 File Modes in Python
# Mode	Description
# 'r'	Read (default) – file must exist
# 'w'	Write – overwrites existing file
# 'a'	Append – adds to end of file
# 'x'	Exclusive – creates a new file
# 'b'	Binary mode (e.g., rb, wb)

# 🧪 Example: Reading a File
# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
# with handles file closing automatically
# read() reads the whole file
# Use readline() or readlines() for line-by-line access

# ✍️ Example: Writing to a File
# with open("data.txt", "w") as file:
#     file.write("Hello, Python!")
# Overwrites if file exists

# 🧱 Appending to a File
# with open("data.txt", "a") as file:
#     file.write("\nNew Line")
# 🧠 Real-Life Analogy:
# File handling is like opening a notebook, writing something, and closing it.
# If you open it in write mode, you tear out old pages and start over!

# 🧹 2. filter() Function – Select items based on condition
# 🔹 What is filter()?
# The filter() function selects elements from a sequence that match a condition.
# It returns an iterator of elements for which the function returns True.

# 🧪 Syntax:
# filter(function, iterable)
# ✅ Example: Filter Even Numbers
# nums = [1, 2, 3, 4, 5, 6]

# def is_even(n):
#     return n % 2 == 0

# even_nums = list(filter(is_even, nums))
# print(even_nums)  # [2, 4, 6]
# 💡 Lambda Shortcut:
# even = list(filter(lambda x: x % 2 == 0, nums))
# 🧠 Real-Life Analogy:
# Like a coffee filter – only the clean liquid passes through, while grounds stay back.

# 🔄 3. map() Function – Transform every item
# 🔹 What is map()?
# The map() function applies a function to each item in an iterable, and returns the result.

# 🧪 Syntax:
# map(function, iterable)
# ✅ Example: Square Numbers
# nums = [1, 2, 3, 4]

# def square(n):
#     return n * n

# squares = list(map(square, nums))
# print(squares)  # [1, 4, 9, 16]
# 💡 Lambda Version:
# squares = list(map(lambda x: x**2, nums))
# 🧠 Real-Life Analogy:
# Like a conveyor belt in a factory — each item gets processed and transformed.

# ➕ 4. reduce() Function – Combine everything into one
# 🔹 What is reduce()?
# reduce() applies a function cumulatively to items in a list and returns a single result.

# It comes from the functools module.

# 🧪 Syntax:
# from functools import reduce
# reduce(function, iterable)
# ✅ Example: Sum of All Elements
# from functools import reduce

# nums = [1, 2, 3, 4, 5]

# total = reduce(lambda a, b: a + b, nums)
# print(total)  # 15
# ➡️ Step-by-step:

# 1 + 2 → 3

# 3 + 3 → 6

# 6 + 4 → 10

# 10 + 5 → 15

# 🧠 Real-Life Analogy:
# Like a cashier adding up your bill — all values are reduced to a total.

# 🔍 Summary Table
# Function	Purpose	Returns	Use Case
# filter()	Select items by condition	Iterator	Pick even numbers, filter data
# map()	Modify every item	Iterator	Square numbers, apply tax
# reduce()	Collapse to one value	Single value	Total sum, max value, product