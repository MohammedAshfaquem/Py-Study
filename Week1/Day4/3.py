# 🧬 Inheritance in Python — Explained in Detail
# ✅ What is Inheritance?
# Inheritance means it  child class can inherit all the properties of parent class
# another class (parent/superclass).

# 🧠 Think of it as:
# "Child inherits everything from parent — and can add or override things."

# 🔧 Why Use It?
# Code Reusability ✅
# Logical Hierarchies ✅
# Cleaner Code ✅

# 🔨 Basic Syntax
# class Parent:
#     # parent code
# class Child(Parent):
#     # child code (inherits from Parent)

# ✅ Simple Example
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speak()  # inherited
# d.bark()   # own method
# 🔁 Types of Inheritance in Python
# Type	Description
# Single	    One child inherits one parent
# Multiple      (careful)One child inherits multiple parents
# Multilevel	Child → Parent → Grandparent
# Hierarchical	Multiple children inherit one parent

# 🔹 1. Single Inheritance
# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")

# b = B()
# b.showA()
# b.showB()
# 🔹 2. Multilevel Inheritance
# class A:
#     def showA(self):
#         print("Class A")

# class B(A):
#     def showB(self):
#         print("Class B")

# class C(B):
#     def showC(self):
#         print("Class C")
# c = C()
# c.showA()
# c.showB()
# c.showC()

# 🔹 3. Hierarchical Inheritanc
# class Parent:
#     def greet(self):
#         print("Hello from parent")

# class Child1(Parent):
#     pass

# class Child2(Parent):
#     pass

# Child1().greet()
# Child2().greet()
# 🔹 4. Multiple Inheritance
# class Father:
#     def skill(self):
#         print("Cooking")

# class Mother:
#     def skill(self):
#         print("Singing")

# class Child(Father, Mother):
#     pass

# c = Child()
# c.skill()
# c.talent()
# Python supports multiple inheritance, but use with care due to the potential for conflicts.

# 🔄 Method Overriding
# If child class defines the same method name as parent, it overrides it:
# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         print("Hello from B")

# b = B()
# b.greet()  # "Hello from B"
# 🔍 Using super()
# Use super() to call parent methods inside child class:
# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         super().greet()
#         print("Hello from B")

# b = B()
# b.greet()
# 🧠 Output:

# Hello from A
# Hello from B
# ✅ Summary
# Feature	    Description
# Inheritance	One class gets features from another
# super()	    Calls parent methods
# Overriding	Child class redefines parent method
# Code Reuse	Avoids writing same logic in every class