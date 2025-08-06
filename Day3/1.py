# 🧠 Python Functions
# ✅ What Is a Function?
# A function in Python is a reusable block of code that performs a specific task.
# Instead of repeating code, you define it once and call it whenever needed.

# 📌 How to Define a Function
# def function_name():
#     # code block
#     print("Hello!")
# ▶️ How to Call a Function
# function_name()  # Output: Hello!
# 🧮 Function with Parameters
# You can pass values (called arguments) into functions:

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Output: Hello, Alice!
# 🔁 Function with Return Value
# Functions can return data using return:
    
# def add(a, b):
#     return a + b

# result = add(5, 3)
# print(result)  # Output: 8
# 🔢 Multiple Parameters and Default Values
# def greet(name="Guest"):
#     print(f"Welcome, {name}!")

# greet("Bob")     # Output: Welcome, Bob!
# greet()          # Output: Welcome, Guest!
# 📋 Summary of Function Components
# Part	Description
# def	Keyword to define a function
# Function name	Name used to call it
# Parameters	Input values for the function
# return	Sends a value back to the caller

# ✨ Example: All Together
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False

# print(is_even(4))  # True
# print(is_even(7))  # False.

# 3️⃣ Built-in Functions (Commonly Used)
# Python comes with many useful built-in functions you can use directly.

# Some popular ones:
# Function	Description	Example
# len()	Length of string, list, etc.	len("hello") → 5
# type()	Return type of an object	type(10) → <class 'int'>
# range()	Generate a sequence of numbers	list(range(3)) → [0,1,2]
# max(), min()	Max or min value in iterable	max([1,5,3]) → 5
# sum()	Sum of numbers in iterable	sum([1,2,3]) → 6
# sorted()	Return sorted list	sorted([3,1,2]) → [1,2,3]
# abs()	Absolute value	abs(-5) → 5

# 4️⃣ Variable Scope
# What is Scope?
# Scope defines where variables can be accessed.

# Local scope: Variables inside a function.

# Global scope: Variables outside all functions.

# Example:
# x = 10  # Global variable

# def my_func():
#     x = 5  # Local variable
#     print(x)

# my_func()   # Prints 5
# print(x)    # Prints 10
# Access global variable inside function:
# x = 10

# def my_func():
#     global x
#     x = 5

# my_func()
# print(x)  # Prints 5 (global changed)


# 🧠 Python Functions: Arguments & Calling
# 1️⃣ Creating a Function
# Define a function using def:
# def greet():
#     print("Hello!")
# 2️⃣ Calling a Function
# Just use the function name with parentheses:
# greet()  # Output: Hello!
# 3️⃣ Arguments and Number of Arguments
# Functions can accept parameters (inputs):
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")  # Output: Hello, Alice!
# If you call with wrong number of arguments, Python raises an error:
# greet()  # TypeError: missing 1 required positional argument: 'name'
# 4️⃣ Arbitrary Arguments: *args
# Use *args to accept any number of positional arguments as a tuple.
# def fruits(*args):
#     for fruit in args:
#         print(fruit)

# fruits("apple", "banana", "cherry")
# # Output:
# # apple
# # banana
# # cherry
# 5️⃣ Keyword Arguments
# Pass arguments with parameter names (keywords):
# def describe_pet(name, animal="dog"):
#     print(f"I have a {animal} named {name}.")

# describe_pet(name="Buddy", animal="cat")
# describe_pet(animal="parrot", name="Polly")
# 6️⃣ Arbitrary Keyword Arguments: **kwargs
# Use **kwargs to accept any number of keyword arguments as a dictionary.
# def person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# person_info(name="Alice", age=30, city="NY")
# # Output:
# # name: Alice
# # age: 30
# # city: NY
# ⚠️ Combining *args and **kwarg
# def example(*args, **kwargs):
#     print("Positional args:", args)
#     print("Keyword args:", kwargs)

# example(1, 2, a=3, b=4)
# # Positional args: (1, 2)
# # Keyword args: {'a': 3, 'b': 4}
# Summary Table
# Feature	Syntax	Description
# Positional arguments	def f(a, b):	Fixed number of arguments
# Arbitrary positional args	def f(*args):	Accept any number of positional args
# Keyword arguments	f(name="John")	Arguments passed by name
# Arbitrary keyword args	def f(**kwargs):	Accept any number of keyword args