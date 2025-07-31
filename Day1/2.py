# 🔹 1. Python Indentation
# 📌 What is indentation?
# Indentation refers to the whitespace (spaces or tabs) at the beginning of a line of code.
# In Python, indentation is not just for readability — it is required.

# 🧠 Why indentation matters in Python?
# Python uses indentation to define blocks (like loops, if, functions).
# Other languages use { } brackets, but Python uses indentation to group code logically.

# ✅ Example:
# # Without indentation (❌ will give error)
# if 5 > 3:
# print("Yes")
# ✅ Correct way (with indentation):

# if 5 > 3:
#     print("Yes")
# 🔍 Rules:
# Standard indentation is 4 spaces per level (tabs are discouraged).

# All lines within the same block must be indented equally.

# Mixing tabs and spaces is not allowed → causes IndentationError.

# ✅ Block Example:
# def greet(name):
#     if name:
#         print("Hello", name)  # Indented inside if
#     else:
#         print("No name")
# ❌ Common Error:
# def func():
#   print("Hi")
#     print("Bye")  # IndentationError: unexpected indent
# 🔧 Best Practices:
# Use 4 spaces (not tabs)

# Be consistent: Don’t mix spaces and tabs

# Configure your editor (VSCode, PyCharm) to insert spaces for tabs.
# 
# 
# 
# 
# 🔹 2. Python Comments
# 🧠 What is a comment?
# A comment is a line in the code that is ignored by the Python interpreter.
# Used to explain code, make notes, or disable parts of code.

# ✅ Single-line Comments:
# Start with #

# # This is a single-line comment
# x = 5  # This is an inline comment
# ✅ Multi-line Comments (2 ways): doesn’t have a real multiline comment syntax like /* */,
# but you can do it using:

# 1. Multiple #:
# # This is line 1
# # This is line 2
# # This is line 3
# 2. Triple quotes (for docstrings or multi-line text):
# """
# This is a multi-line string
# used as a comment or documentation
# """
# 🔹 Note: Triple-quoted strings are not true comments.
# They are actually string literals, but if unused, Python ignores them.

# 🧪 Example with both:
# # Define a function
# def add(a, b):
#     """
#     This function returns the sum of two numbers.
#     """
#     return a + b  # Return the result
# 📌 Summary
# Feature	Description
# Indentation	Required to define blocks of code
# Default spaces	4 spaces per level (don’t mix tabs!)
# Comments	Use # for single-line
# Multi-line docs	Use """ ... """ or multiple # lines