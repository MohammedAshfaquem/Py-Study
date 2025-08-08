# 🛑 What is Exception Handling?
# An exception is an error that occurs during the execution of a program and disrupts the normal flow of the code.
# Python provides tools to catch and handle errors, so your program doesn’t crash unexpectedly.

# ⚠️ Common Exceptions:
# Exception Type	   Description
# ZeroDivisionError	   Dividing by zero
# TypeError	           Wrong data type used
# ValueError	       Invalid value (e.g., letters in int())
# IndexError	       Index out of range
# KeyError	           Dictionary key not found
# FileNotFoundError	   File doesn’t exist

# ✅ Basic Syntax of Exception Handling
# try:
#     # code that might cause an error
# except SomeException:
#     # code to run if error happens
# 📌 Example 1: Handling ZeroDivisionError
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# 📌 Example 2: Handling multiple exceptions
# try:
#     number = int("abc")
#     print(10 / 0)
# except ValueError:
#     print("Invalid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# 🔄 else and finally
# You can also use else and finally blocks:

# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print("That's not a number!")
# else:
#     print("Good, you entered:", x)
# finally:
#     print("This runs no matter what.")
# Block	When it runs
# try	    Code that may raise an error
# except	Runs if an exception happens
# else	    Runs if no error occurred
# finally	Always runs (cleanup code like closing files)

# 📌 Example 3: Catching all exceptions (not always recommended)
# try:
#     x = 1 / 0
# except Exception as e:
#     print("An error occurred:", e)
# 💡 Catching general Exception is helpful during debugging, but avoid using it in production unless necessary.

# ✅ Summary
# Use try/except to prevent program crashes
# Handle specific exceptions when possible
# Use else for code that runs only if no error
# Use finally for cleanup tasks