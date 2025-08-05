# 🔹 Simple Definition of Polymorphism
# Polymorphism means "many forms."
# In programming, polymorphism allows different classes to be treated as if they were the same class, through a common interface, even though their behavior may differ.

# 🔑 Key Points of Polymorphism
# Key Concept	Description
# "Many Forms"	Same method name behaves differently for different classes
# Common Interface	Classes follow a shared structure (often via inheritance or duck typing)
# Dynamic Behavior	Actual method executed is determined at runtime
# Method Overriding	Child class defines its own version of a method inherited from a parent
# Code Reusability	Reduces duplication by allowing unified function/method calls
# Duck Typing (Python)	If it "quacks like a duck," it’s treated as a duck — no need for strict types

# 🧠 Two Main Types of Polymorphism in Python
# 1. Compile-Time Polymorphism (not native in Python)
# Also called method overloading.

# Python doesn't support traditional overloading — instead, we use default arguments or *args.

# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c

# calc = Calculator()
# print(calc.add(2, 3))        # 5
# print(calc.add(2, 3, 4))     # 9
# 2. Run-Time Polymorphism (native in Python)
# Achieved through method overriding and duck typing.

# Useful with inheritance and common method names.

# class Animal:
#     def speak(self):
#         print("Some generic animal sound")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

# # Polymorphic behavior
# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.speak()  # Calls the correct version of speak()
# 🔎 Output:
# Bark
# Meow
# Some generic animal sound
# Even though we’re calling the same method speak(), each class behaves differently — this is polymorphism.

# 🦆 Duck Typing in Python
# “If it looks like a duck and quacks like a duck, it must be a duck.”

# Python is dynamically typed, so you don’t need inheritance to achieve polymorphism.

# class Duck:
#     def walk(self):
#         print("Duck walks")

# class Human:
#     def walk(self):
#         print("Human walks")

# def let_it_walk(thing):
#     thing.walk()  # Doesn’t care what type 'thing' is

# let_it_walk(Duck())
# let_it_walk(Human())
# 🔎 Output:
# Duck walks
# Human walks
# This is polymorphism without inheritance — Python cares about behavior, not type.

# ✅ Summary Table
# Term	Meaning
# Polymorphism	Ability of different objects to respond to the same method call in different ways
# Method Overloading	Same method name with different arguments (limited in Python)
# Method Overriding	Subclass changes the method defined in the parent class
# Duck Typing	If an object has the right method, Python doesn't care what type it is

# 💡 Real-World Analogy
# Think of polymorphism like the word “drive”:

# A car drives on the road.

# A boat drives in water.

# A golf ball drives down the fairway.

# Different "things" respond to the same command (“drive”), but behave differently.



# # ✅ Summary Table
# # Type	Example
# # Built-in Polymorphism	len() works with string, list, etc.
# # Method Overriding	Child class overrides parent method
# # Duck Typing	Function accepts any object with method
# # Class-based	Same method name, different class output.


# # Why is Polymorphism Important?
# # Extensibility: You can add new classes without changing existing code.
# # Maintainability: Write generic functions that work on any compatible object.
# # Code clarity: The same method name means the same action, customized per class.
# # Flexibility: Allows frameworks and libraries to work with user-defined classes.


