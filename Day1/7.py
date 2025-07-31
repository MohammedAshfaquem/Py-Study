# 🔁 What are Loops in Python?
# Loops are used to repeat a block of code multiple times.

# Real-life example:
# Imagine you want to say "Hello" to 5 people — instead of writing the print statement 5 times, you use a loop.

# 🔹 Types of Loops in Python
# Python supports two main types of loops:

# Loop Type	Description
# for loop	Iterate over a sequence (list, string, range)
# while loop	Run as long as a condition is True

# 1️⃣ for Loop
# 🔸 Syntax:
# for variable in sequence:
#     # code block
# 🔸 Example:
# for i in range(5):
#     print("Hello", i)
# 🧠 Explanation:

# range(5) generates numbers: 0, 1, 2, 3, 4

# Each time, i takes a value from that range

# Output:
# Hello 0
# Hello 1
# Hello 2
# Hello 3
# Hello 4
# 📦 Common Iterables in for loops:
# list: for fruit in ["apple", "banana"]:
# string: for ch in "hello":
# tuple, set, dict, range(), etc.

# 🧠 Real-life Analogy:
# You have 3 chocolates in a box.
# for choco in chocolates: – you pick one chocolate at a time.

# 2️⃣ while Loop
# 🔸 Syntax:
# while condition:
#     # code block
# 🔸 Example:
# i = 0
# while i < 5:
#     print("Hi", i)
#     i += 1
# 🧠 Explanation:

# Starts with i = 0

# Runs as long as i < 5

# i += 1 increases the value of i

# Output:
# Hi 0
# Hi 1
# Hi 2
# Hi 3
# Hi 4
# 🧠 Real-life Analogy:
# You play a game while your battery > 20%.
# while battery > 20: keep playing!

# 🔃 Loop Control Statements
# Keyword	 Meaning
# break	     Stops the loop completely
# continue	 Skips current iteration, moves to next
# pass	     Does nothing (placeholder)

# 🔸 Example of break
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# 🧠 Output:

# Copy
# Edit
# 0 1 2 3 4
# 🔸 Example of continue
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# 🧠 Output:

# Copy
# Edit
# 0 1 3 4
# 🔸 Example of pass
# for i in range(3):
#     pass  # do nothing
# 🧠 pass is used when you haven’t written the logic yet, but the syntax needs something.  ✅✅✅✅✅✅✅✅✅✅✅✅

# ✅ Summary Table:
# Feature	for loop	while loop
# When to use	When iterating over sequence	When repeating till condition is true
# Condition checked	Before every iteration	Before every iteration
# Can use break?	Yes	Yes
# Can use continue?	Yes	Yes