# 🔹 What is a Data Type?
# A data type in Python defines the kind of value a variable holds and what operations can be performed on it.

# 🗂️ Python Built-in Data Types (Core Categories)
# Category	Types Included
# Numeric	int, float, complex
# Sequence	str, list, tuple, range
# Set	    set, frozenset
# Mapping	dict
# Boolean	bool
# Binary	bytes, bytearray, memoryview
# None Type	NoneType (only None)

# 🔢 1. Numeric Types
# ✅ int — Integer
# Whole numbers

# No decimal
# a = 10
# ✅ float — Floating point
# Decimal values
# pi = 3.14
# ✅ complex — Complex numbers
# Format: real + imagj
# z = 3 + 4j
# 🔤 2. Text Type
# ✅ str — String
# Sequence of characters, enclosed in quotes
# name = "Ashfaque"
# ✅ Strings are immutable

# 📚 3. Sequence Types
# ✅ list
# Ordered
# Mutable (can change)

# Heterogeneous elements (mixed types)
# fruits = ["apple", "banana", 5]
# ✅ tuple
# Ordered
# Immutable
# coords = (10, 20)
# ✅ range
# Generates a sequence of numbers
# r = range(5)  # 0 to 4
# 🔁 4. Set Types
# ✅ set
# Unordered, no duplicates

# Mutable
# s = {1, 2, 3}
# ✅ frozenset
# Immutable version of a set

# 📌 5. Mapping Type
# ✅ dict
# Stores key-value pairs

# Unordered (in Python 3.6 and below), ordered (3.7+)
# person = {"name": "John", "age": 30}
# ⚡ 6. Boolean Type
# ✅ bool
# Values: True or False
# is_active = True
# Used in conditions, loops, etc.

# 🧵 7. Binary Types
# Work with binary data (like files, images)

# Type	Description
# bytes	Immutable array of bytes
# bytearray	Mutable array of bytes
# memoryview	Memory view of byte array
# b = b"hello"
# ba = bytearray([65, 66, 67])
# ❌ 8. NoneType
# ✅ None
# Special type representing the absence of a value
# x = None
# Used when:

# Function doesn’t return anything

# Placeholder for optional values

# 🧪 Example Summar
# a = 10            # int
# b = 3.14          # float
# c = 2 + 3j        # complex
# name = "Ash"      # str
# lst = [1, 2, 3]   # list
# tup = (1, 2)      # tuple
# s = {1, 2}        # set
# d = {"a": 1}      # dict
# flag = True       # bool
# n = None          # NoneType
# 📌 Mutable vs Immutable Types
# Type	Mutable?
# int, float	❌ No
# str	❌ No
# tuple	❌ No
# list	✅ Yes
# dict	✅ Yes
# set	✅ Yes

# 🔁 Type Conversion
# Python allows conversion between data types:
# int("10")      # 10
# float("5.6")   # 5.6
# str(123)       # "123"
# list("abc")    # ['a', 'b', 'c']
# set([1, 2, 2]) # {1, 2}
# 🧠 Real-Life Analogy
# Real-world object	Python Data Type	Why?
# Mobile contacts	dict	key (name) → value (number)
# Shopping bag	list	ordered, can add/remove
# ID card	tuple	fixed info, unchangeable
# Attendance sheet	set	unique names only
# Light switch	bool	on/off = True/False

# 📌 Summary Table
# Data      Type	Description	        Mutable
# int	    Whole number	            No
# float  	Decimal number	            No
# complex	Complex numbers         	No
# str	    Text	                    No
# list  	Ordered collection	        Yes
# tuple	    Ordered, fixed collection	No
# dict	    Key-value pairs	            Yes
# set	    Unordered unique values 	Yes
# bool	    True/False	                No
# NoneType	No value	                No