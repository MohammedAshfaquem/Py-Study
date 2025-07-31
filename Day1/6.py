# 🔸 Python Conditional Statements
# ✅ 1. if Statement
# x = 10
# if x > 5:
#     print("x is greater than 5")
# 🔹 Explanation:

# Python checks the condition x > 5

# If it's True, it runs the indented code below it

# If not, it skips that block

# ✅ 2. if-else Statement
# x = 3
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is 5 or less")
# 🔹 Explanation:

# If if condition is True, first block runs

# Otherwise, the else block executes

# ✅ 3. if-elif-else (multiple conditions)
# x = 7
# if x > 10:
#     print("Greater than 10")
# elif x > 5:
#     print("Greater than 5 but not more than 10")
# else:
#     print("5 or less")
# 🔹 Explanation:

# Checks if first → if False,

# Then checks elif → if False,

# Then finally runs else

# 🔹 Note: Only one block executes (the first one that is True)

# 🔸 Indentation Rule in Conditions
# x = 8
# if x > 5:
#     print("Big")
#     print("Really big")
# print("Done")
# ✅ Only indented lines under the if block are conditional.
# ✅ print("Done") will always run — not inside the if.

# 🔸 4. match-case Statement (🔰 Python 3.10+)
# This is Python’s version of switch-case.

# ✅ Syntax:
# value = 2

# match value:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Something else")
# 🔹 Explanation:

# match compares value to each case

# _ is like default — if no other matches, run this

# ✅ With pattern matching:
# person = ("Alice", 25)

# match person:
#     case ("Alice", age):
#         print(f"Alice is {age} years old")
#     case (_, age):
#         print(f"Someone is {age} years old")
# 💡 Real-Life Analogy:
# if-elif-else is like asking yes/no questions one by one.

# match-case is like having one answer and checking which case it matches — more organized for many values.