# What is a String in Python?
# A string in Python is a sequence of characters enclosed in quotes. Strings are used to represent text data.
# How to create strings?
# You can create strings using:
# Single quotes '...'
# Double quotes "..."
# Triple quotes '''...''' or """...""" for multi-line strings

# s1 = 'Hello'
# s2 = "World"
# s3 = '''This is
# a multi-line
# string'''
# Key points about strings:
# Strings are immutable — once created, you cannot change their individual characters.
# You can access characters by index.
# Strings support many useful methods for text processing.

# Examples:
# greeting = "Hello, World!"
# print(greeting)          # Hello, World!
# print(type(greeting))    # <class 'str'>
# print(greeting[0])       # H  (first character)
# print(len(greeting))     # 13 (length of the string)

# 1. Accessing Characters (Indexing)
# Strings are sequences, so you can access characters by index.
# 2. Slicing Strings
# Get a substring using start:stop:step syntax.
# s = "Hello, World!"
# 3. Modifying Strings
# Strings are immutable (can't change in-place), but you can create new strings:
# s = "Hello"
# # Replace character by rebuilding string:
# s = s[:1] + "a" + s[2:]
# print(s)  # Hallo
# print(s[0:5])    # Output: Hello   (characters 0 to 4)
# print(s[:5])     # Same as above
# print(s[7:])     # Output: World!
# print(s[::2])    # Output: Hlo ol! (every 2nd char)
# print(s[::-1])   # Output: !dlroW ,olleH (reversed string).

# 4. Concatenating Strings
# Combine strings with + or other methods:
# a = "Hello"
# b = "World"
# print(a + " " + b)  # Hello World

# # Using join
# words = ["Hello", "World"]
# print(" ".join(words))  # Hello World.

# 5. Important String Methods
# Method	Description	Example
# .lower()	Convert to lowercase	"Hi".lower() → "hi"
# .upper()	Convert to uppercase	"Hi".upper() → "HI"
# .strip()	Remove whitespace from ends	" hi ".strip() → "hi"
# .replace(old, new)	Replace substring	"cat".replace("c", "b") → "bat"
# .split(sep)	Split into list by separator	"a,b,c".split(",") → ['a','b','c']   string to list ✅✅✅✅✅✅✅✅
# .join(iterable)	Join iterable of strings with this as separator	"-".join(["a","b"]) → "a-b"  list to string ✅✅✅✅✅
# .find(sub)	Find index of substring (or -1)	"apple".find("p") → 1
# .startswith(prefix)	Check if string starts with prefix	"hello".startswith("he") → True
# .endswith(suffix)	Check if string ends with suffix	"hello".endswith("lo") → True..


# Advanced .1️⃣ String Formatting in Python
# a) f-strings (Python 3.6+)
# Use f"..." and embed expressions inside {}:
# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")
# # Output: My name is Alice and I am 30 years old.
# You can also do calculations inside {}:
# print(f"In 5 years, I will be {age + 5}.")
# b) .format() method
# Older way but still useful:
# print("My name is {} and I am {} years old.".format(name, age))
# # Output: My name is Alice and I am 30 years old.
# print("Coordinates: {lat}, {lon}".format(lat=50.5, lon=20.1))


# 2️⃣ Regular Expressions (using re module)
# Used for powerful pattern matching and text searching.
# import re

# text = "My phone number is 123-456-7890."

# # Search for a pattern (digits with dashes)
# match = re.search(r"\d{3}-\d{3}-\d{4}", text)

# if match:
#     print("Phone number found:", match.group())
# else:
#     print("No phone number found.")
# Common re functions:

# Function	Description
# re.search()	Find first match
# re.findall()	Find all matches
# re.match()	Match at start of string
# re.sub()	Replace pattern in string

# 3️⃣ Advanced String Slicing and Manipulation
# a) Extended slicin
# s = "Hello, World!"

# print(s[7:12])    # Output: World
# print(s[::-1])    # Output: !dlroW ,olleH  (reversed string)
# print(s[::2])     # Output: Hlo ol! (every 2nd character)
# b) String methods for manipulation
# Method	What it does	Example
# .replace(a, b)	Replace substring a with b	"cat".replace("c", "b") → "bat"
# .split(sep)	Split string into list by separator	"a,b,c".split(",") → ['a','b','c']
# .join(iterable)	Join list of strings with separator	"-".join(["a","b","c"]) → "a-b-c"

# c) Example: Reverse each word in a sentenc
# sentence = "Hello world"
# reversed_words = " ".join(word[::-1] for word in sentence.split())
# print(reversed_words)  # Output: "olleH dlrow"