# 🧠 Types of Variables in Python
# In Python, variables can be categorized based on:

# Scope (where they are accessible)
# Lifetime (how long they exist)
# Location (inside or outside functions)

# 🔹 1️⃣ Global Variables
# Declared outside any function.
# Can be accessed anywhere in the file (even inside functions).
# x = 10  # Global variable

# def show():
#     print(x)

# show()  # Output: 10
# ❗ To modify a global variable inside a function:
# count = 0

# def increment():
#     global count
#     count += 1

# increment()
# print(count)  # Output: 1
# 🔹 2️⃣ Local Variables
# Declared inside a function.
# Only accessible within that function.
# def greet():
#     name = "Alice"  # Local variable
#     print("Hello", name)

# greet()
# # print(name)  ❌ Error: name is not defined
# 🔹 3️⃣ Nonlocal Variables (used inside nested functions)
# Not global, but also not local to inner function.
# Declared in outer function, used in nested function.

# def outer():
#     message = "Hello"

#     def inner():
#         nonlocal message
#         message = "Hi"

#     inner()
#     print(message)

# outer()  # Output: Hi
# 🔹 Summary Table
# Variable Type	Defined in	Accessible in	Use global / nonlocal?
# Global	Outside function	Whole file (and inside functions with global)	Use global to modify
# Local	Inside function	Only in that function	N/A
# Nonlocal	Outer function (in nested setup)	Inner function	Use nonlocal
