# 🔷 Abstraction – Simple Definition
# Abstraction means hiding unnecessary details and showing only the relevant features to the user.

# 🧠 Key Points of Abstraction
# Concept	Description
# Hides     complexity	Internal code/logic is hidden from the user
# Shows only essentials	Only relevant methods/data are shown
# Improves readability	Cleaner and more user-friendly code
# Used via abstract classes	In Python, using abc module
# Enforces design	Forces child classes to implement required methods

# 🐍 Python Implementation of Abstraction
# Python supports abstraction through the abc (Abstract Base Class) module.
# 1. Abstract Class
# Cannot be instantiated (you can't create an object of it).
# May contain abstract methods (methods without implementation).

# 2. Abstract Method
# A method with no body (implementation).
# Must be implemented in the subclass.

# ✅ Example:
# from abc import ABC, abstractmethod

# # Abstract class
# class Vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# # Child class must implement the abstract methods
# class Car(Vehicle):
#     def start(self):
#         print("Car started")

#     def stop(self):
#         print("Car stopped")

# c = Car()
# c.start()
# c.stop()
# If you try to create an object of Vehicle, Python will throw an error:
# ❌ TypeError: Can't instantiate abstract class Vehicle with abstract methods

# 🧱 Why Use Abstraction?
# To define a clear interface for future developers.

# To ensure child classes follow a structure.

# To hide internal logic and prevent misuse.

# 🧑‍🏫 Real-Life Analogy:
# Example	Abstraction View
# ATM Machine	You only see options like Withdraw, Deposit, etc. Internals are hidden
# Mobile App	You tap buttons — you don’t see how they work in code
# TV Remote	You press volume buttons, but don’t see how signals work inside

# 🔁 Summary Table
# Feature	        Description
# Abstraction	    Hiding internal logic and showing only necessary parts
# Abstract class	A base class with at least one abstract method
# Abstract method	Method with no implementation (must be overridden)
# abc module	    Used in Python to implement abstraction
# Real benefit	    Cleaner, structured, and more maintainable code.

from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
    
# class B(A):
#     def start(self):
#         print("B Started")
#     def stop(self):
#         print("b Stopped")        
# b = B()
# b.start()
# b.stop()

