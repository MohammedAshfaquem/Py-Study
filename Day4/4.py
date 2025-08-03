# 🌀 Polymorphism in Python
# ✅ What is Polymorphism?
# Polymorphism means "many forms" — the same function or method behaves differently depending on the object calling it.

# It's about writing flexible and reusable code.

# 🔍 Real-life Analogy:
# The word “draw” means different things:

# 🎨 An artist draws with a pencil

# 🧊 A freezer drawer pulls out

# 🏹 A warrior draws a bow

# → Same name, different behavior

# 🧱 Example 1: Built-in Polymorphis
# print(len("Ashfaque"))      # 8 (string length)
# print(len([1, 2, 3]))        # 3 (list length)
# print(len({"a": 1, "b": 2})) # 2 (dict length)
# ✅ The function len() behaves differently based on the type of object.

# 🧱 Example 2: Polymorphism with Classe
# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# animals = [Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())
# 🧠 Even though both objects use speak(), they respond in their own way.

# 🧱 Example 3: Polymorphism with Inheritanc
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")

# class Car(Vehicle):
#     def move(self):
#         print("Car is driving")

# class Boat(Vehicle):
#     def move(self):
#         print("Boat is sailing")

# # Polymorphism in action
# for v in [Car(), Boat()]:
#     v.move()
# 📌 The move() method behaves differently depending on the subclass, even though it’s the same method name.

# ✅ Method Overriding → A Type of Polymorphism
# When a child class redefines a method from the parent, it’s called method overriding.
# class Person:
#     def greet(self):
#         print("Hello!")

# class Student(Person):
#     def greet(self):
#         print("Hi, I'm a student!")

# Student().greet()  # Overrides parent
# ✅ Duck Typing (Dynamic Polymorphism)
# "If it walks like a duck and quacks like a duck, treat it like a duck."
# class File:
#     def open(self):
#         print("File opened")

# class Camera:
#     def open(self):
#         print("Camera opened")

# def start(obj):
#     obj.open()

# start(File())
# start(Camera())
# ✅ We don’t care what the object is — as long as it has an .open() method, it works.

# ✅ Summary Table
# Type	Example
# Built-in Polymorphism	len() works with string, list, etc.
# Method Overriding	Child class overrides parent method
# Duck Typing	Function accepts any object with method
# Class-based	Same method name, different class output.


# Why is Polymorphism Important?
# Extensibility: You can add new classes without changing existing code.
# Maintainability: Write generic functions that work on any compatible object.
# Code clarity: The same method name means the same action, customized per class.
# Flexibility: Allows frameworks and libraries to work with user-defined classes.