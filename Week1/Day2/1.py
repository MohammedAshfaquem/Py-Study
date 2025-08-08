# 🔄 What is Mutability in Python?
# Mutability means an object can be changed after it is created.

# If you can change the content of an object (like add, remove, or modify elements), it is mutable.

# If you cannot change its content after creation, it is immutable.

# 🧠 Think of This Real-Life Analogy:
# Mutable = Whiteboard → You can erase and rewrite.

# Immutable = Paper printout → Once printed, you cannot change the text.

# ✅ Mutable Data Types in Python:
# Type	Can Be Changed?	Example
# list	✅ Yes	[1, 2, 3] → [1, 2, 99]
# dict	✅ Yes	{'a': 1} → {'a': 10}
# set	✅ Yes	{1, 2} → {1, 2, 3}
# bytearray	✅ Yes	Used in binary data operations

# ❌ Immutable Data Types in Python:
# Type	Can Be Changed?	Example
# int	❌ No	a = 5 → a = 6 (new object)
# float	❌ No	3.14 → 2.71 creates new value
# bool	❌ No	True → False = new object
# str	❌ No	"hello" → "hell" creates new
# tuple	❌ No	(1, 2) → can't modify inside
# frozenset	❌ No	Immutable version of set
# bytes	❌ No	Used for binary strings

# 🔬 How to Check If an Object is Mutable?
# Try modifying it — or use this example:

# a = [1, 2, 3]
# print(id(a))     # original ID
# a.append(4)
# print(id(a))     # same ID → mutable

# x = "hello"
# print(id(x))     # original ID
# x += " world"
# print(id(x))     # new ID → immutable
# ✅ list kept same ID → changed in place
# ❌ str created new ID → changed by re-creating

# 🔁 Mutable Example – list
# fruits = ['apple', 'banana']
# fruits.append('mango')
# print(fruits)  # ['apple', 'banana', 'mango']
# 🔹 You changed the same object.

# ❌ Immutable Example – str
# name = "Ashfaque"
# name[0] = 'M'  # ❌ Error: 'str' object does not support item assignment
# ⚠️ Danger with Mutability – Shared References
# a = [1, 2, 3]
# b = a  # both point to same list
# b.append(4)
# print(a)  # [1, 2, 3, 4] 😱 changed 'a' too!
# To avoid this, use:

# b = a.copy()
# 🎯 Why Does It Matter?
# Mutable types can be modified in-place. Useful for performance, but risky with shared data.

# Immutable types are safer (e.g., for keys in dictionaries) and thread-safe.

# Summary Table:
# Type	Mutable?	Example
# list	✅	[1, 2, 3]
# dict	✅	{"a": 1}
# set	✅	{1, 2, 3}
# tuple	❌	(1, 2, 3)
# str	❌	"hello"
# int, float	❌	42, 3.14