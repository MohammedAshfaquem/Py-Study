# 🔹 What is an Iterator?
# An iterator is an object that allows you to traverse through a sequence, one element at a time.
# In simple terms:
# It remembers where it left off in a sequence
# You use the built-in functions iter() and next() to control it

# 🔧 Key Terminology
# Term	Meaning
# Iterable	Any object you can loop over (like list, tuple, string, etc.)
# Iterator	An object with __iter__() and __next__() methods
# iter()	Function to convert iterable → iterator
# next()	Returns the next item from the iterator

# 📦 How Iterators Work Internally
# Step-by-step:
# nums = [1, 2, 3]         # Iterable
# it = iter(nums)          # Convert to iterator

# print(next(it))          # 1
# print(next(it))          # 2
# print(next(it))          # 3
# print(next(it))          # ❌ StopIteration error
# Each call to next(it) gives the next value

# When items are exhausted → StopIteration exception is raised

# 🧱 Creating a Custom Iterator
# To create a custom iterator, define a class with:

# __iter__(self) → returns the iterator object itself

# __next__(self) → returns the next value or raises StopIteration

# class Count:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         val = self.current
#         self.current += 1
#         return val

# # Usage
# c = Count(1, 5)
# for num in c:
#     print(num)
# 🔁 Output:
# 1
# 2
# 3
# 4
# 5
# 🧠 Real-Life Analogy
# Think of a TV remote:
# You press "Next" to move to the next channel
# The remote “remembers” where you are
# Once channels are over, it stops
# That’s how an iterator works — one item at a time, and it remembers position.

# 🔄 Iterators vs Iterables
# Feature	Iterable	Iterator
# What it is	Collection of items	Object that traverses items
# Has __iter__()	✅ Yes	✅ Yes
# Has __next__()	❌ No	✅ Yes
# Example	list, string, tuple	object returned by iter()

# ⚡ Iterator vs Generator
# Feature	Iterator Class	Generator Function
# Syntax	Class with __next__()	Uses yield
# Memory Efficient	❌ Not always	✅ Yes
# Simpler to write	❌ No (requires boilerplate)	✅ Yes

# 🔸 Use generators when: you want to write lightweight iterators easily

# 🔐 Why Iterators Matter
# ✅ Allows efficient looping over large data
# ✅ Can make your own data structures iterable
# ✅ Supports lazy evaluation (don’t load everything at once)
# ✅ Powers Python’s for loop under the hood

# 🧪 Iterator Mini Quiz (5 Questions)
# Q1. Which method must be defined for an object to become an iterator?
# a) __get__()
# b) __len__()
# c) __next__()
# d) __init__()

# ✅ Answer: c

# Q2. What does iter(obj) return?
# a) A list
# b) A generator
# c) An iterator
# d) A function

# ✅ Answer: c

# Q3. What happens when next() is called after items are exhausted?
# a) It repeats the first item
# b) It raises a StopIteration exception
# c) It crashes the program
# d) It restarts the loop

# ✅ Answer: b