# 🧱 What Are Classes and Objects in Python?
# 🔹 1. What is a Class?
# A class is a blueprint or template for creating objects.

# It defines:
# What data an object should hold (called attributes).
# What Functions an object can perform (called methods).

# Think of a class as a cookie cutter, and objects as the cookies 🍪 made from it.

# ✅ Example Class Definition
# class Person:
#     def __init__(self, name, age):  # Constructor
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hi, I'm {self.name} and I'm {self.age} years old.")
# 🔹 2. What is an Object?
# An object is an instance of a class — a real thing created based on the class.
# p1 = Person("Ashfaque", 25)  # Object 1
# p2 = Person("Sana", 22)      # Object 2

# p1.greet()  # Output: Hi, I'm Ashfaque and I'm 25 years old.
# p2.greet()  # Output: Hi, I'm Sana and I'm 22 years old.
# 🔎 What’s Happening Behind the Scenes?
# 👉 __init__() is a constructor:
# Automatically called when a new object is created.
# self refers to that specific object instance.
# self.name and self.age are instance variables unique to each object.

# 🧠 Understanding self
# It refers to the current object.
# Allows each object to keep track of its own data.
# def greet(self):
#     print(self.name)  # Access the object’s name
# ✅ Example: Car Clas
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def drive(self):
#         print(f"Driving {self.brand} {self.model}")

# # Create objects
# c1 = Car("Toyota", "Corolla")
# c2 = Car("Tesla", "Model 3")

# c1.drive()  # Driving Toyota Corolla
# c2.drive()  # Driving Tesla Model 3
# 🎯 Why Use Classes and Objects?
# Feature	    Benefit
# Reusability	One class can create many objects
# Organization	Code is cleaner and grouped logically
# Real-world    mapping	Models real-world entities and behavior

# 🔄 Class vs Object Summary
# Concept	Description	Example
# Class	    Template or blueprint	Person class
# Object	Instance of a class	p1 = Person(...)
# Method	Function inside a class	greet(self)
# Attribute	Variable tied to an object	self.name     a




# 🔸 1. Class Variables vs Instance Variables
# ✅ Instance Variables
# Defined inside __init__
# Unique to each object
# Use self.
# class Car:
#     def __init__(self, brand):
#         self.brand = brand  # instance variable
# c1 = Car("Toyota")
# c2 = Car("Tesla")
# print(c1.brand)  # Toyota
# print(c2.brand)  # Tesla


# ✅ Class Variables
# Defined outside any method, usually at the top of the class
# Shared by all objects
# class Car:
#     wheels = 4  # class variable

#     def __init__(self, brand):
#         self.brand = brand  # instance variable

# c1 = Car("Toyota")
# c2 = Car("Tesla")

# print(c1.wheels)  # 4
# print(c2.wheels)  # 4

# Car.wheels = 6
# print(c1.wheels)  # 6 (updated for all)
# Type	Belongs To	Defined Where
# Instance variable	Each object	Inside __init__
# Class variable	Whole class	Directly in class body

# 🔸 2. Method Types in Python Classes
# ✅ 1. Instance Method
# Takes self as first argument
# Can access both instance & class variables

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):  # instance method
#         print(f"Hi, I'm {self.name}")
# ✅ 2. Class Method
# Takes cls as first argument
# Uses @classmethod decorator
# Can access class variables

# class Dog:
#     count = 0
#     def __init__(self):
#         Dog.count += 1

#     @classmethod
#     def total_dogs(cls):
#         print(f"Total dogs: {cls.count}")

# ✅ 3. Static Method
# Doesn’t take self or cls
# Uses @staticmethod decorator
# Just a utility function inside the class

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
# print(Math.add(3, 4))  # 7
# Method Type	     Uses	Can Access
# Instance Method	 self	Instance & class data
# Class Method	     cls	Only class data
# Static Method	     None	No instance/class data