# ✅ What is a Dictionary in Python?
# Python dictionary = JavaScript object

# Both store key-value pairs.

# person = {
#     "name": "Ashfaque",
#     "age": 25
# }
# ✅ 1. Access Items
# print(person["name"])     # Output: Ashfaque
# print(person.get("age"))  # Output: 25

# ✅ 2. Change Items
# person["age"] = 26
# ✅ 3. Add Items
# person["email"] = "ashfaque@mail.com"
# ✅ 4. Remove Items
# del person["age"]
# # OR
# person.pop("name")
# delete person.age;
# ✅ 5. Loop Through Dictionary
# for key in person:
#     print(key, person[key])
# ✅ 6. Dictionary Comprehension (🔥 Like JS map/filter for objects)
# 🎯 Example 1: Square of numbers
# nums = [1, 2, 3]
# squares = {n: n**2 for n in nums}
# print(squares)  # {1: 1, 2: 4, 3: 9}
# 🎯 Example 2: Filter only even values
# even_squares = {n: n**2 for n in nums if n % 2 == 0}
# print(even_squares)  # {2: 4}
# ✅ 7. Important dict Methods
# Python Method	Description	JavaScript Equivalent
# get(key)	Get value for key	obj[key] or obj.key
# keys()	Get all keys	Object.keys(obj)
# values()	Get all values	Object.values(obj)
# items()	Get all key-value pairs	Object.entries(obj)
# update(dict2)	Merge dict2 into original	Object.assign(obj1, obj2)
# pop(key)	Remove item with key	delete obj[key]
# clear()	Remove all items	obj = {}
# copy()	Shallow copy	{...obj}

# 🧪 Example:
# person = {"name": "Ash", "age": 25}
# print(person.keys())      # dict_keys(['name', 'age'])
# print(person.values())    # dict_values(['Ash', 25])
# print(person.items())     # dict_items([('name', 'Ash'), ('age', 25)])
# 🧠 In Simple Words:
# Python dict is just like a JS object.

# Keys must be unique, and values can be any data type.

# Use comprehension for advanced filtering or transformation.