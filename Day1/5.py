# 🔹 What are Operators?
# Operators are special symbols used to perform operations on variables and values.

# ✅ Real-Life Example:
# Just like:

# + means add in math,

# In Python, a + b adds the values of a and b.

# 🔸 Types of Operators in Python:
# Category	Description
# 1. Arithmetic	Mathematical operations
# 2. Assignment	Assign values
# 3. Comparison	Compare values
# 4. Logical	Combine conditions (True/False logic)
# 5. Identity	Check object identity
# 6. Membership	Check if value is part of sequence
# 7. Bitwise	Binary-level operations

# ✅ 1. Arithmetic Operators (math-based)
# Operator	Meaning	Example	Result
# +	Addition	3 + 2	5
# -	Subtraction	3 - 2	1
# *	Multiplication	3 * 2	6
# /	Division	3 / 2	1.5
# //	Floor Division	5 // 2	2
# %	Modulus	5 % 2	1
# **	Exponent	2 ** 3	8

# 🔹 Floor Division // gives the integer part only.
# 🔹 Modulus % gives the remainder.

# ✅ 2. Assignment Operators (assign value)
# Operator	Example	Meaning
# =	x = 5	Assign 5 to x
# +=	x += 3	x = x + 3
# -=	x -= 2	x = x - 2
# *=	x *= 2	x = x * 2
# /=	x /= 2	x = x / 2
# //=	x //= 2	x = x // 2
# %=	x %= 2	x = x % 2
# **=	x **= 2	x = x ** 2

# ✅ 3. Comparison Operators (returns True/False)
# Operator	Example	Meaning
# ==	a == b	Equal
# !=	a != b	Not Equal
# >	a > b	Greater Than
# <	a < b	Less Than
# >=	a >= b	Greater Than or Equal
# <=	a <= b	Less Than or Equal

# 📌 Used mostly in conditions (if, loops, etc.)

# ✅ 4. Logical Operators (combine conditions)
# Operator	Meaning	Example	Result
# and	True if both true	a > 2 and a < 10	True
# or	True if any one true	a < 2 or a > 10	True
# not	Reverse condition	not(a > 2)	False

# 🎯 Think like decision making:

# "Is the person adult and has ticket?"

# ✅ 5. Identity Operators
# Operator	Meaning	Example	Result
# is	    True if same object	x is y	True/False
# is not	True if not same object	x is not y	True/False

# 🧠 Difference between value and object:
# a = [1, 2]
# b = a
# c = [1, 2]

# a is b  # True → same object
# a is c  # False → different object
# a == c  # True → values are same
# ✅ 6. Membership Operators
# Operator	Meaning	Example	Result
# in	    True if value in sequence	'a' in 'apple'	True
# not in	True if value not in sequence	'x' not in 'apple'	True

# 🔍 Checks if an item is present in a list, string, tuple, etc.

# ✅ 7. Bitwise Operators (advanced)
# Operator	Meaning	Example (5 = 0101, 3 = 0011)	Result
# &	AND	5 & 3 → 0001	1
# `	`	OR	`5
# ^	XOR	5 ^ 3 → 0110	6
# ~	NOT	~5 → -(5+1)	-6
# <<	Left Shift	5 << 1 → 1010	10
# >>	Right Shift	5 >> 1 → 0010	2

# 📌 Used in low-level programming (image processing, security, etc.)

# ✨ Summary Table
# Type	        Key Use
# Arithmetic	Numbers/math
# Assignment	Store/update values
# Comparison	Conditional checks
# Logical   	Combine multiple conditions
# Identity   	Check same object
# Membership	Check if value exists in sequence
# Bitwise	    Binary-level operations