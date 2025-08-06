# 🔹 What is a Variable in Python?
# A variable is a named reference to a value stored in memory.
# Think of it like:
# 🪣 A label (x) stuck on a container that holds a value (10)

# Example:
# x = 10
# x is the variable (label)
# 10 is the value
# Python stores 10 in memory and x points to it

# ✅ Key Features of Python Variables
# 1. Dynamically Typed
# You don’t need to declare the type of a variable:

# x = 10      # int
# x = "hello" # now it's a string
# 👉 The type of variable is decided at runtime, based on the value.

# 2. No Need for Declaration
# No need to write int x; or String x; like in Java or C++.
# Just assign:

# name = "Ashfaque"
# age = 25
# 3. Variables are Just Labels
# In Python, variables don’t store the actual value.
# They store a reference (pointer) to the object in memory.

# 🔍 Example:
# x = [1, 2, 3]
# y = x
# y.append(4)
# print(x)  # Output: [1, 2, 3, 4]
# Why?
# x and y point to the same list object in memory.

# 🧠 Behind the Scenes:
# x = 10
# Steps:

# Python creates an integer object 10 in memory.
# It binds the name x to that object.
# The type of the object is int.

# 🔠 Variable Naming Rules
# ✅ Valid:
# Must start with a letter (a-z or A-Z) or underscore _
# Can contain letters, digits (0-9), and underscores
# Case-sensitive (age ≠ Age)

# ❌ Invalid:
# Cannot start with a number (e.g., 1num)
# Cannot use special characters like @, $, %
# Cannot use Python keywords like if, for, class

# 🧪 Examples:
# # Valid
# name = "John"
# _age = 25
# total_amount_2 = 500

# # Invalid
# 2name = "error"      # ❌ starts with a number
# class = "Math"       # ❌ 'class' is a keyword
