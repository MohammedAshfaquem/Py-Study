# 🎨 Python Decorators — Explained Simply
# ✅ What Is a Decorator?
# A decorator is a function that:
# Takes another function as input
# Adds extra functionality to it
# And returns a new function (or the same, modified one)

# It’s like “wrapping” a gift (function) with more behavior — without changing the original function.

# 🔧 Basic Syntax of a Decorator
# def decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()
#         print("After the function runs")
#     return wrapper


# Use it like this:
# @decorator
# def say_hello():
#     print("Hello!")

# say_hello()
# 🔍 Output:
# Before the function runs
# Hello!
# After the function runs
# 🔁 How It Works Behind the Scenes
# This:

# @decorator
# def greet():
#     print("Hi!")
# Is the same as:

# def greet():
#     print("Hi!")

# greet = decorator(greet)
# 📌 Decorator with Arguments
# To allow the inner function to accept arguments:

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before call")
#         result = func(*args, **kwargs)
#         print("After call")
#         return result
#     return wrapper

# @decorator
# def add(a, b):
#     return a + b

# print(add(3, 4))
# 🔍 Output:
# Before call
# After call
# 7
# 🧠 Real-world Example: Logging
# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def multiply(a, b):
#     return a * b

# print(multiply(2, 5))
# ✨ Built-in Decorators Examples
# Decorator   	Purpose
# @staticmethod	Defines a static method in a class
# @classmethod	Defines a method with access to the class (cls)
# @property	    Treats a method like a read-only attribute

# 🔁 Summary
# Decorators are used to modify or enhance functions without changing them.
# They use the @ syntax.
# They’re often used for:
# Logging
# Authentication
# Timing
# Caching
# Input validation

# To Lower Case:
# def main(fun):
#     def findVowels(name):
#         if isinstance(name,str):
#             fun(name.lower());
#         else:
#             print("Invalid Input")
#     return findVowels;
    
# @main
# def Pass(name):
#     print(f"Name is {name}");
    
# Pass("Ashfaqeu");


#  To Find Vowels:
# def main(fun):
#     def findVowels(name):
#         total =0
#         low = name.lower();
#         for i in low:
#             if i in 'aeiou':
#                 total +=1
#         fun(total)
#     return findVowels;
    
# @main
# def Pass(count):
#     print(f"Vowels {count}");
    
# Pass("Ashfaque")