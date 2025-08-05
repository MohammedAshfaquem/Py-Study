# Great question! You're talking about method resolution in multiple inheritance — a key part of Python's OOP behavior.

# Let’s first break this down and then solve your specific question.

# 👨‍👩‍👧 Multiple Inheritance in Python
# In your example:

# class Father:
#     def skill(self):
#         print("Cooking")

# class Mother:
#     def talent(self):
#         print("Singing")

# class Child(Father, Mother):
#     pass
# Calling c.skill() or c.talent() works because Child inherits from both Father and Mother.

# ❓ If Both Parents Have the Same Method Name
# Let’s say both parents have a skill() method:

# class Father:
#     def skill(self):
#         print("Father: Cooking")

# class Mother:
#     def skill(self):
#         print("Mother: Dancing")

# class Child(Father, Mother):
#     pass
# Now, calling:

# c = Child()
# c.skill()
# Will output:

# makefile
# Copy
# Edit
# Father: Cooking
# Because of Python’s Method Resolution Order (MRO) — it looks from left to right in the inheritance list (Father first).

# ✅ How to Specifically Call a Parent’s Method?
# You can directly call a method from a specific parent class using the class name:

# class Child(Father, Mother):
#     def use_father_skill(self):
#         Father.skill(self)

#     def use_mother_skill(self):
#         Mother.skill(self)
# Then:

# c = Child()
# c.use_father_skill()  # Father: Cooking
# c.use_mother_skill()  # Mother: Dancing
# 🧠 Summary:
# Goal	Solution
# Default method call	Follows MRO (left to right)
# Call specific parent's method	ParentClass.method(self)

# Would you like to explore how MRO is computed with Child.__mro__ or super()?



# You said:
# yes

# ChatGPT said:
# Awesome — let's dig into MRO (Method Resolution Order) and super() in Python. These are powerful tools in multiple inheritance.

# 🔁 What Is MRO?
# MRO stands for Method Resolution Order — it's the order in which Python looks for methods or attributes when a class is called.

# Python uses the C3 linearization algorithm to determine this order, especially in complex multiple inheritance situations.

# 🧪 Example: MRO in Action
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.show()  # Which one gets called?
# To check MRO:

# print(D.__mro__)
# Output:

# kotlin
# Copy
# Edit
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# So d.show() will print "B" because B appears before C.

# 🧭 Using super()
# super() gives you a way to call the next method in MRO, rather than hardcoding the parent class name.

# 🎯 Example Using super():
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")
#         super().show()  # calls A.show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()  # calls A.show()

# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()  # calls B.show(), which calls C.show(), which calls A.show()

# d = D()
# d.show()
# Output:
# D
# B
# C
# A
# 💡 Notice that super() in each class automatically follows the MRO chain — no need to specify which parent class.

# ✅ Summary:
# Concept	Description
# __mro__	Tuple showing class resolution order
# super()	Calls next method in the MRO chain
# Python's rule	Left-to-right based on inheritance order, but follows C3 linearization