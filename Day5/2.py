# 🔹 What is a Generator?
# A generator is a special type of function that returns an iterator and allows you to iterate over data without storing the entire dataset in memory.
# It’s like a smart version of a function that pauses and resumes.

# ✅ Key Features of Generators
# Feature	         Description
# Uses yield	     Instead of return, it uses yield to pause
# Memory efficient	 Doesn’t store all values at once
# Lazy evaluation	 Produces one value at a time on demand
# Automatically      becomes an iterator	No need to define __iter__ or __next__

# 🧠 Real-Life Analogy
# Think of a water cooler:

# You press the tap (call next()), and it gives one cup of water (one value)

# It waits until you press again

# Water is not pre-poured, it comes when you ask

# That’s exactly how a generator works.

# 🔄 Generator vs Normal Function
# Feature	Normal Function	Generator Function
# Uses return	✅ Yes	❌ No
# Uses yield	❌ No	✅ Yes
# Returns value	All at once	One value at a time
# Stops	After return	After yield, resumes later

# 🧪 Example 1: Simple Generator
# def simple_gen():
#     yield 1
#     yield 2
#     yield 3

# g = simple_gen()
# print(next(g))  # 1
# print(next(g))  # 2
# print(next(g))  # 3
# # print(next(g))  # ❌ Raises StopIteration
# 🧱 Example 2: Generator with Loop
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1

# for num in countdown(5):
#     print(num)
# 🔁 Output:

# Copy
# Edit
# 5
# 4
# 3
# 2
# 1
# Each time the loop runs, it resumes from where it last paused

# 🧠 How it works internally
# Every generator:

# Keeps track of its state

# Resumes where it left off after each yield

# Raises StopIteration when done

# 🚀 Generator Expressions (One-liners)
# Like list comprehensions but more memory-efficient:

# gen = (x**2 for x in range(5))
# for val in gen:
#     print(val)
# ✅ Output:

# Copy
# Edit
# 0
# 1
# 4
# 9
# 16
# Unlike [x**2 for x in range(5)], this doesn’t store all values — it creates one at a time.

# 🔁 Generator vs Iterator
# Feature	Iterator Class	Generator Function
# Syntax	Class + __next__()	Function + yield
# Easy to write	❌ No	✅ Yes
# Use case	Custom logic	Large data / streams
# Auto state tracking	❌ Manual	✅ Automatic

# 🧾 Why Use Generators?
# ✅ Efficient for large data (like logs, files)
# ✅ Saves memory
# ✅ Great for infinite sequences
# ✅ Simple and readable

# 🔐 Common Use Cases
# Reading large files line by line

# Infinite sequences (e.g., Fibonacci)

# Streams of data (APIs, sensors)

# Replacing complex iterator classes

# 💡 Real-World Example: Read File with Generator
# def read_file_line_by_line(filename):
#     with open(filename) as f:
#         for line in f:
#             yield line.strip()

# for line in read_file_line_by_line("bigfile.txt"):
#     print(line)
# ✅ Reads without loading the whole file into memory!

# 📝 Mini Quiz – Generators
# Q1. What keyword is used in a generator function?
# a) return
# b) next
# c) yield
# d) pass

# ✅ Answer: c

# Q2. What is returned when you call a generator function?
# a) A list
# b) A generator object
# c) A tuple
# d) A string

# ✅ Answer: b

# Q3. Which of these is true about generators?
# a) They are slower than lists
# b) They use more memory
# c) They compute values on the fly
# d) They return all values at once

# ✅ Answer: c

# Q4. What happens when a generator is exhausted?
# a) It restarts
# b) It returns None
# c) It raises StopIteration
# d) It deletes itself

# ✅ Answer: c

# Q5. What does this generator output?
# def test():
#     yield "Hi"
#     yield "Bye"

# g = test()
# print(next(g))
# ✅ Answer: Hi

# ✅ Summary
# Concept	Meaning
# Generator	Function that returns an iterator using yield
# Lazy Eval	Only computes values when needed
# Memory Safe	Doesn’t store full sequences
# Better Than	Traditional iterators (in many cases)