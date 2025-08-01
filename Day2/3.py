# 🔷 What is a Tuple?
# A tuple is a collection of items that:
# Is ordered (items have a fixed position)
# Is immutable (you cannot change items once created)
# Can store any data type (strings, numbers, etc.)
# Uses parentheses ( ) to define

# 📦 Think of a tuple like a sealed box. Once packed, you can’t change what’s inside — only read it.
# my_tuple = ("apple", "banana", "cherry")
# 🧩 Tuple Synta
# t = ("apple", "banana", "cherry")
# ✅ You can also have different types:
# t = (1, "hello", 3.5, True)
# ⚠️ If you want a single-item tuple, you must use a comma:
# t = ("apple",)   # ✅ This is a tuple
# t = ("apple")    # ❌ This is just a string
# 🧠 Why Use Tuples?
# ✅ Faster than lists
# ✅ Safe (data won’t change accidentally)
# ✅ Good for constants, coordinates, database rows


# ✅ 1. Access Tuple Items
# You can access items using indexing like lists:
# my_tuple = ("apple", "banana", "cherry")
# print(my_tuple[0])  # Output: apple
# print(my_tuple[-1]) # Output: cherry
# You can also use slicing:
# print(my_tuple[1:3])  # Output: ('banana', 'cherry')


# 🔒 2. Update Tuples (Not Directly)
# Tuples are immutable, so you can’t directly update their elements:
# my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
# ✅ But you can convert to a list, change, then convert back:
# temp = list(my_tuple)
# temp[0] = 10
# my_tuple = tuple(temp)
# print(my_tuple)  # Output: (10, 2, 3)


# 🔁 3. Loop Through Tuples
# You can use a loop just like with lists:
# fruits = ("apple", "banana", "cherry")

# for item in fruits:
#     print(item)

# # Output:
# # apple
# # banana
# # cherry
# Or with index:
# for i in range(len(fruits)):
#     print(fruits[i])


# 🧰 4. Important Tuple Methods
# Tuples have fewer methods than lists because they are immutable.

# Method	Description	Example
# .count(x)	Returns number of times x appears	(1,2,2,3).count(2) → 2
# .index(x)	Returns index of first occurrence of x	(1,2,3).index(2) → 1

# 6️⃣ Nested Tuples (Tuple inside Tuple)
# nested = ((1, 2), (3, 4), (5, 6))
# print(nested[0][1])  # 2

# Example:
# t = (1, 2, 2, 3, 4)
# print(t.count(2))  # 2
# print(t.index(3))  # 3rd element, index 2
# 🧠 Bonus: Tuple Packing & Unpackin
# # Packing
# person = ("Alice", 25)

# # Unpacking   enn paranja js destructuring ad list tuple possible ann object verumbo .values() .keys() okke use aakanam   ✅✅✅✅✅✅✅✅✅
# name, age = person
# print(name)  # Alice
# print(age)   # 25
# ✅ Summary Table
# Feature	Tuple	List
# Mutable?	❌ No	✅ Yes
# Syntax	(1, 2, 3)	[1, 2, 3]
# Faster?	✅ Yes (performance)	❌ No
# Methods	.count(), .index() only	Many methods like .append()