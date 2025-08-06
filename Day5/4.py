# 🔹 What is zip()?
# The zip() function combines multiple iterables (lists, tuples, etc.) into a single iterator of tuples, element-wise.

# ✅ Basic Example:
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 90, 95]

# for pair in zip(names, scores):
#     print(pair)
# 🟢 Output:
# ('Alice', 85)
# ('Bob', 90)
# ('Charlie', 95)
# 🧠 With Dictionary Comprehension
# names = ['Alice', 'Bob', 'Charlie']
# scores = [85, 90, 95]

# result = {name: score for name, score in zip(names, scores)}
# print(result)
# ✅ Output:

# {'Alice': 85, 'Bob': 90, 'Charlie': 95}
# 🔍 Key Points:
# Stops at the shortest list

# Very useful for building dictionaries
# Works well inside loops, comprehensions

# 🔹 What Are Magic Methods?
# Magic methods are special methods with names that start and end with double underscores, like __init__, __str__, __add__.
# They allow custom objects to:
# Support built-in operators (+, ==, len())
# Define object creation and representation

# Hook into Python's syntax features

# 🧠 Real-Life Analogy:
# Think of a class like a machine.
# Magic methods are hidden gears that make it interact smoothly with Python's tools like print(), +, ==, len().

# 🔧 Categories of Magic Methods
# 1️⃣ Object Lifecycle
# Method	Purpose
# __init__	Constructor (initial setup)
# __new__	Creates instance (rarely used)
# __del__	Destructor (called on delete)

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print("Person created:", self.name)

#     def __del__(self):
#         print(f"{self.name} is being deleted")
# p = Person("Alex")
# del p  # triggers __del__
# 2️⃣ String Representations
# Method	Purpose
# __str__	For print(obj) — user-friendly string
# __repr__	Official string, for debugging/logging

# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def __str__(self):
#         return f"{self.brand} Car"

#     def __repr__(self):
#         return f"Car('{self.brand}')"

# c = Car("Tesla")
# print(c)        # Tesla Car       → uses __str__
# print(repr(c))  # Car('Tesla')    → uses __repr__
# 3️⃣ Operator Overloading
# You can define how your object behaves with operators like +, -, ==, <, etc.

# Operator	Magic Method
# +	__add__
# -	__sub__
# *	__mul__
# ==	__eq__
# <	__lt__
# len()	__len__

# class Book:
#     def __init__(self, pages):
#         self.pages = pages

#     def __add__(self, other):
#         return Book(self.pages + other.pages)

#     def __str__(self):
#         return f"Book with {self.pages} pages"

# b1 = Book(100)
# b2 = Book(200)
# b3 = b1 + b2
# print(b3)  # Book with 300 pages
# 4️⃣ Length, Indexing, and Iteration
# Function	Magic Method
# len()	__len__
# obj[i]	__getitem__
# Loop	__iter__, __next__

# class MyList:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, index):
#         return self.data[index]

# ml = MyList([10, 20, 30])
# print(len(ml))     # 3
# print(ml[1])       # 20
# 5️⃣ Callable Objects
# Feature	Method
# Function call	__call__()

# class Greet:
#     def __call__(self, name):
#         print(f"Hello, {name}!")

# g = Greet()
# g("Alice")  # Hello, Alice!
# 🧠 Why Use Magic Methods?
# ✅ Make classes behave like built-ins
# ✅ Operator overloading
# ✅ Control how objects are created, displayed, and used
# ✅ Cleaner, more Pythonic code

# 🧱 Full Example with Multiple Magic Methods
# class Counter:
#     def __init__(self, count):
#         self.count = count

#     def __str__(self):
#         return f"Counter({self.count})"

#     def __add__(self, other):
#         return Counter(self.count + other.count)

#     def __eq__(self, other):
#         return self.count == other.count

#     def __len__(self):
#         return self.count

# a = Counter(5)
# b = Counter(10)
# print(a + b)        # Counter(15)
# print(a == b)       # False
# print(len(a))       # 5


# | Feature                 | Pass by Value                                   | Pass by Reference                          |
# | ----------------------- | ----------------------------------------------- | ------------------------------------------ |
# | **Type of Argument**    | A **copy** of the value is passed               | A **reference** (memory address) is passed |
# | **Effect of Changes**   | Changes do **not affect** the original variable | Changes **affect** the original variable   |
# | **Python's Behavior**   | **Pass by Value** for immutable objects         | **Pass by Reference** for mutable objects  |
# | **Example (Immutable)** | `int`, `str`, `tuple`                           | N/A                                        |
# | **Example (Mutable)**   | N/A                                             | `list`, `dict`, `set`                      |

# 4️⃣ Types of Functions (Based on Arguments and Return Values)
# 🔧 4 Types:
# Type	Description	Example
# No argument, no return	Only performs task	Print message
# Argument, no return	Takes input, does something, no return	Print square
# No argument, return	Doesn’t take input, gives output	Return fixed value
# Argument, return	Takes input, returns output	Add two numbers

# ✅ Examples for Each:
# 1. No Arg, No Return:
# def greet():
#     print("Hello!")
# 2. Arg, No Return:
# def square(x):
#     print(x * x)
# 3. No Arg, Return:
# def get_pi():
#     return 3.14
# 4. Arg + Return:
# def add(a, b):
#     return a + b.

# 🔹 What is Monkey Patching?
# Monkey Patching refers to the dynamic modification or extension of a class or module at runtime.
# This means you can  add functionality to an already existing class or method without modifying the original source code.
# The term "monkey patching" is used to describe this technique because you’re kind of "tweaking" or "hacking" parts of the code while it is running.

# In Python, this means you can replace or modify methods and attributes of classes, functions, or even modules at runtime. It can be used to add behavior, fix bugs, or change implementation without altering the original source code.

# 🔹 Why Use Monkey Patching?
# Use Cases:
# Hotfixes: You can fix a bug in an external module without changing the source.
# Enhancing functionality: Add extra functionality to an existing class or function.
# Testing: Modify objects or methods for mocking or patching during tests.
# Legacy code: When you cannot modify the source, you can patch behavior for compatibility.

# 🔹 How Does Monkey Patching Work in Python?
# In Python, everything is object-oriented and dynamic, so we can assign new methods to classes or replace methods of existing objects at runtime.

# Key Points:
# We can change methods and attributes of existing classes.
# Monkey patching doesn’t modify the original source code, just the running instance.
# It works on mutable objects like classes and functions.

# ✅ Basic Example: Monkey Patching a Method
# Suppose you have a class that has a method greet and you want to change its behavior after the class has been defined.
# class Greeter:
#     def greet(self):
#         print("Hello!")

# # Patching the 'greet' method at runtime
# def new_greet(self):
#     print("Hi there!")

# # Monkey patch: Replacing the 'greet' method with 'new_greet'
# Greeter.greet = new_greet

# # Now, calling greet will use the patched version
# g = Greeter()
# g.greet()  # Output: Hi there!
# Here:

# We replace the greet method in the Greeter class with the new new_greet method.

# Now, the class Greeter no longer uses the original greet method but the new version.

# ✅ Example: Monkey Patching a Module
# We can also apply monkey patching to modules. For example, let's say you want to add extra functionality to Python's built-in math module.
# import math

# # Original behavior
# print(math.sqrt(16))  # Output: 4.0

# # Monkey Patching the sqrt method
# def new_sqrt(x):
#     print(f"Calculating sqrt of {x}")
#     return math.sqrt(x)

# # Patching sqrt
# math.sqrt = new_sqrt

# # Now, the new patched method is used
# print(math.sqrt(16))  # Output: Calculating sqrt of 16 \n 4.0
# Here:

# We modify the sqrt function in the math module to add logging before calling the original function.

# 🔹 Advantages of Monkey Patching
# Quick Fixes: You can quickly fix bugs or issues in a third-party library without needing to change the original source code.
# Custom Behavior: Add or modify behavior dynamically at runtime to meet new requirements.
# Testing: When mocking or overriding parts of an application for testing, monkey patching is very useful.
# Compatibility: Modify existing code to be compatible with newer versions or different frameworks.

# 🔹 Disadvantages of Monkey Patching
# Hard to Maintain: It can make your code difficult to maintain because it relies on dynamic changes that aren't clearly visible in the original code.
# Confusing for Others: If someone else is reading your code, they may not immediately understand the patch or why it was applied.
# Potential Conflicts: If you patch a method or class that is later updated (e.g., in a new version of a library), your patch may cause conflicts or break the program.
# Dangerous in Production: In production, it can be risky since it changes code behavior unexpectedly.

# 🔹 Real-Life Analogy:
# Think of Monkey Patching like changing the engine of a running car.
# Imagine you're driving a car (your program) and you realize the engine (a method or function) needs an upgrade or fix. Instead of stopping the car and redesigning the engine from scratch, you simply swap out the engine parts while the car is running.

# While this might be fast and effective in the short term, it can lead to unpredictable outcomes and maintenance challenges over time.

# 🔹 When Should You Use Monkey Patching?
# Best Scenarios:
# For quick fixes in third-party libraries where the source code is unavailable or inaccessible.

# For testing — to mock or patch parts of your code during unit testing.

# When working with legacy systems that can’t be directly modified, but you need to add or tweak behavior.

# Avoid Using It:
# In production environments unless absolutely necessary. It can introduce unexpected behaviors and make code harder to maintain.

# When creating large or complex systems, as it can lead to confusion about what code is actually executing.

# 🧪 Optional Mini Quiz (Test Your Understanding)
# Here’s a mini quiz to help solidify your understanding of Monkey Patching.

# Q1: What is the primary risk of using Monkey Patching?
# a) It increases the code readability
# b) It can lead to conflicts and unexpected behavior in the future
# c) It makes the code faster
# d) It reduces the need for unit testing

# Q2: Which of the following is an example of Monkey Patching?
# a) Modifying the code of an imported library directly
# b) Replacing a method in an existing class at runtime
# c) Writing unit tests for an external library
# d) Importing functions from another module

# Q3: What is the advantage of using Monkey Patching?
# a) It makes the code easier to read
# b) It allows you to quickly fix bugs in third-party libraries without modifying source code
# c) It removes the need for imports
# d) It is only used for debugging purposes

# Q4: Can you Monkey Patch methods of built-in modules in Python?
# a) Yes
# b) No

# Q5: When should Monkey Patching be avoided?
# a) In production code unless necessary
# b) When writing unit tests
# c) In small projects or during rapid prototyping
# d) In libraries that are under active development

# ✅ Answers:
# b) It can lead to conflicts and unexpected behavior in the future.

# b) Replacing a method in an existing class at runtime.

# b) It allows you to quickly fix bugs in third-party libraries without modifying source code.

# a) Yes.

# a) In production code unless necessary.


