# 🔹 What is Encapsulation?
# Encapsulation means binding data and methods into a single unit (a class), and restricting direct access
# to some of the object’s components.

# In simple terms, it’s like putting important things inside a box and only allowing access through specific rules.

# 🎯 Main Goal of Encapsulation
# To protect the internal state of an object from unintended or harmful modification.
# To control how the data is accessed or modified using methods (getters and setters).

# ✅ Key Points of Encapsulation
# Key Point	Description
# 🔒 Hides internal data	Prevents direct access to sensitive data
# 🧱 Data + functions bundled	Keeps related logic in one class
# 🛡️ Protects object integrity	Keeps data consistent and safe
# 👮 Control access	Uses methods to validate/modify data
# 🚦 Uses access modifiers	Like public, _protected, __private

# 🧠 Real-Life Analogy
# Think of a bank ATM:

# You can’t access the money inside directly

# You must use an interface (buttons/screen) to interact

# Your PIN is private, and only you can use it

# That's encapsulation — it hides the internal data and exposes only what's needed.

# 🐍 Encapsulation in Python
# Python does not enforce access restrictions like other languages (Java, C++),
# but it follows naming conventions:

# Access    Type	    Syntax Example	Meaning
# Public	self.name	Accessible from anywhere
# Protected	self._name	Suggests "use with caution"
# Private	self.__name	Not directly accessible (name mangling)

# 🧪 Example in Python
# class Person:
#     def __init__(self, name, age):
#         self.name = name             # Public
#         self._id = 101               # Protected
#         self.__salary = 50000        # Private

#     def display(self):
#         print(f"Name: {self.name}, ID: {self._id}")

#     def get_salary(self):           # Getter
#         return self.__salary

#     def set_salary(self, new_salary):   # Setter with condition
#         if new_salary > 0:
#             self.__salary = new_salary
#         else:
#             print("Invalid salary")

# p = Person("Alice", 30)

# # Access public and protected
# print(p.name)         # ✅ Works
# print(p._id)          # ✅ Works (but discouraged)

# # print(p.__salary)   # ❌ Fails: AttributeError
# print(p.get_salary()) # ✅ Correct way to access private data

# p.set_salary(60000)   # ✅ Modify safely
# print(p.get_salary()) # 60000
# 🧾 Benefits of Encapsulation
# ✅ Clean code structure
# ✅ Controlled access to sensitive data
# ✅ Prevents misuse or corruption of data
# ✅ Easier debugging and maintenance
# ✅ Supports abstraction and security

# 🧩 Encapsulation vs Abstraction
# Feature	    Encapsulation	                       Abstraction
# Focus      	How to restrict access	               How to hide complexity
# Tools used	Access modifiers, getters/setters	   Abstract classes, interfaces
# Goal      	Protect data	                       Simplify interface

# 📝 Mini Quiz (1 Question)
# Q: Which of the following is TRUE about encapsulation?

# a) It hides implementation and exposes only functionality
# b) It allows direct access to private variables
# c) It is not possible in Python
# d) It separates class and methods

# ✅ Answer: a) It hides implementation and exposes only functionality
# 📝 Encapsulation ensures that class attributes are accessed through safe interfaces.

# Would you like:

# A coding exercise on encapsulation?

# A comparison between encapsulation and inheritance?

# Or the next topic: Inheritance explained deeply?

# Let me know how you'd like to continue!



# You said:
# i want more q 

# ChatGPT said:
# Perfect! Here's a full quiz on Encapsulation — with a mix of theory and code-based questions to help you test your understanding like a pro.

# 🧠 Encapsulation Quiz in Python
# (10 Questions with explanations)
# 🔹 Q1. What is encapsulation mainly used for?
# a) To increase runtime speed
# b) To hide implementation and protect data
# c) To allow method overloading
# d) To automatically generate code

# ✅ Answer: b
# 📝 Encapsulation protects internal data and allows access only through controlled interfaces.

# 🔹 Q2. Which symbol is used in Python to define a private variable?
# a) _ (single underscore)
# b) __ (double underscore)
# c) !
# d) @@

# ✅ Answer: b
# 📝 Double underscores __ trigger name mangling, making variables private to the class.

# 🔹 Q3. What will be the output?
# class Test:
#     def __init__(self):
#         self.__x = 10

# t = Test()
# print(t.__x)
# a) 10
# b) Error
# c) 0
# d) None

# ✅ Answer: b
# 📝 Private variable __x is not directly accessible. It will raise AttributeError.

# 🔹 Q4. Which of the following is NOT a benefit of encapsulation?
# a) Data protection
# b) Code modularity
# c) Faster execution
# d) Controlled access to data

# ✅ Answer: c
# 📝 Encapsulation doesn't speed up execution; it's about design, safety, and structure.

# 🔹 Q5. What does the following line represent?
# self._balance = 1000
# a) Private variable
# b) Public variable
# c) Protected variable
# d) Constant

# ✅ Answer: c
# 📝 The _ prefix is a convention that indicates "protected" — use with care.

# 🔹 Q6. Which method allows safe access to a private variable?
# a) A constructor
# b) A getter method
# c) A print statement
# d) An abstract method

# ✅ Answer: b
# 📝 Getter methods (like get_balance()) allow safe, controlled access to private data.

# 🔹 Q7. Choose the correct way to access a private variable using name mangling:
# class A:
#     def __init__(self):
#         self.__secret = 42

# a = A()
# a) a.secret
# b) a.__secret
# c) a._A__secret
# d) a.secret__

# ✅ Answer: c
# 📝 Name mangling renames __secret to _A__secret inside the class.

# 🔹 Q8. What is wrong with this code?
# class Car:
#     def __init__(self):
#         self.__speed = 100

# car = Car()
# car.__speed = 200
# print(car.__speed)
# a) It will print 200
# b) It modifies the private variable
# c) It creates a new public variable
# d) It will raise an error

# ✅ Answer: c
# 📝 car.__speed = 200 creates a new public variable, doesn't affect the private __speed.

# 🔹 Q9. Which of the following statements best defines encapsulation in OOP?
# a) Encapsulation separates objects
# b) Encapsulation limits reuse
# c) Encapsulation binds code and data together while controlling access
# d) Encapsulation hides classes from use

# ✅ Answer: c

# 🔹 Q10. When should you use encapsulation?
# a) When you want to keep internal data secure
# b) When your class only has public variables
# c) When you want to overload operators
# d) When writing scripts, not classes

# ✅ Answer: a
# 📝 Encapsulation is ideal for keeping internal state safe and exposing only what's needed.