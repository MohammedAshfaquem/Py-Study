# 🔁 1️⃣ Recursion in Python
# ✅ What is recursion?
# Recursion is when a function calls itself to solve a smaller part of the problem.

# 💡 Example: Factorial
# def factorial(n):
#     if n == 0:
#         return 1    Base Case
#     else:
#         return n * factorial(n - 1) Recursive Case

# print(factorial(5))  # Output: 120
# factorial(5) → 5 × factorial(4)

# factorial(4) → 4 × factorial(3) ...

# Until factorial(0) returns 1 (base case)

# ⚠️ Recursive Function Must Have:
# Base case → when to stop

# Recursive call → function calls itself.

# ⚡ 2️⃣ Lambda Functions (Anonymous functions)
# ✅ What is a Lambda?
# A lambda function is a one-line, unnamed function.

# 🧪 Syntax:
# lambda arguments: expression
# 🔹 Example 1: Simple square function
# square = lambda x: x * x
# print(square(5))  # Output: 25
# 🔹 Example 2: Used in map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # [1, 4, 9, 16]
# 🔹 Example 3: Used in filter()
# evens = list(filter(lambda x: x % 2 == 0, nums))
# print(evens)  # [2, 4]
# 🔹 Example 4: Used in sorted() with key
# names = ["Alice", "Bob", "Charlie"]
# names_sorted = sorted(names, key=lambda x: len(x))
# print(names_sorted)  # ['Bob', 'Alice', 'Charlie']
# 🔄 Recap
# Feature	Recursion	                        Lambda Functions
# Use case	Solving problems by breaking down	Short, inline functions
# Has name?	Yes (named function)	            No (anonymous)
# Syntax	def + function name	                lambda args: expression
# Example	factorial(n)	                    lambda x: x*x