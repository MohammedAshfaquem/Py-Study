# 🔒 1️⃣ Python Closures
# ✅ What is a Closure?
# A closure is a function object that remembers values from its enclosing scope even after the outer function has finished execution.

# In short: A nested function that can access variables from its outer function, even after the outer function is done running.

# 🔹 Closure Example:
# def outer(x):
#     def inner(y):
#         return x + y
#     return inner

# add5 = outer(5)   # x = 5 is remembered
# print(add5(3))    # Output: 8
# print(add5(10))   # Output: 15
# ✅ Here, x is from the outer scope, and it's remembered by inner.

# 💡 When to Use Closures?
# When you want a function that remembers some data

# Useful in decorators, factories, and callback functions

# 🌐 2️⃣ Python Namespace
# ✅ What is a Namespace?
# A namespace is a container that holds names (variables, functions, etc.) and maps them to objects (like memory locations).

# Python uses different namespaces to keep things organized and avoid name conflicts.

# 🔹 Types of Namespaces
# Namespace Type	Description
# Local	Inside a function (local variables)
# Enclosing	In outer function (for nested functions)
# Global	Top-level of your script or module
# Built-in	Python's built-in names (like len, print)

# 📌 Example:
# x = "global"

# def outer():
#     x = "enclosing"

#     def inner():
#         x = "local"
#         print(x)   # local

#     inner()
#     print(x)       # enclosing

# outer()
# print(x)           # global
# ✅ This illustrates LEGB Rule:
# When Python looks for a variable, it searches in this order:

# Local

# Enclosing

# Global

# Built-in

# 🧠 Visual of LEGB
# def outer():         ← Enclosing namespace
#     def inner():     ← Local namespace
#         print()      ← Python searches: Local → Enclosing → Global → Built-in
# ✅ Summary
# Concept	Use for
# Closure	Creating functions that remember values from outer scope
# Namespace	Managing variable scopes and avoiding name collisions