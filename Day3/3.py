# ✅ What is a Module?
# A module in Python is simply a file containing Python code (functions, variables, classes, etc.) that you can import and reuse in other Python programs.

# Any .py file is a module.

# Helps keep your code organized, reusable, and modular.

# 🧠 Why Use Modules?
# Avoid repeating code
# Organize large projects
# Reuse your own code across files
# Use powerful built-in or third-party functionality

# 🔹 1. Importing a Module
# a) Import whole module
# import math

# print(math.sqrt(16))   # Output: 4.0
# print(math.pi)         # Output: 3.141592...
# b) Import specific parts
# from math import sqrt, pi

# print(sqrt(25))        # 5.0
# print(pi)              # 3.1415...
# c) Rename a module (aliasing)
# import math as m

# print(m.factorial(5))  # 120
# 🔹 2. Creating Your Own Module
# Suppose you have a file named myutils.py:

# # myutils.py
# def greet(name):
#     return f"Hello, {name}!"

# def add(a, b):
#     return a + b
# Now, in another file:

# # main.py
# import myutils

# print(myutils.greet("Alice"))    # Hello, Alice!
# print(myutils.add(3, 4))         # 7
# ✅ Both .py files should be in the same folder (or use Python packages for structure).

# 🔹 3. Built-in Python Modules
# Python includes many built-in modules. Examples:

# Module	Purpose
# math	    Mathematical functions
# random	Random number generation
# datetime	Dates and times
# os	    Interacting with the operating system
# sys	    System-specific parameters and tools
# re	    Regular expressions
# json	    Work with JSON data

# Example: Using random module
# import random

# print(random.randint(1, 10))     # Random int between 1 and 10
# print(random.choice(['a', 'b'])) # Randomly pick from list
# 🔹 4. Using dir() and help()
# You can explore a module’s content:

# import math
# print(dir(math))    # List all functions/attributes
# help(math.sqrt)     # Info about sqrt
# 🔸 Bonus: __name__ == "__main__" in Modules
# When you create a module, you can make part of it run only when the module is run directly, not when imported:

# # myutils.py
# def greet(name):
#     return f"Hello, {name}!"

# ✅ When to use it?
# Use if __name__ == "__main__" to:
# it run only that file run when other file is acces and running this it deos not run

# Write test code

# Run sample output

# Prevent execution when importing modules

# if __name__ == "__main__":
#     print(greet("Direct run"))  # This runs only if you run myutils.py directly
# ✅ Summary
# Action	Syntax / Example
# Import a module	import math
# Import specific functions	from math import sqrt
# Create your own module	Write a .py file with functions
# List module contents	dir(module_name)
# Get help for a function	help(function)