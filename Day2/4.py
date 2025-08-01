# ✅ 1. What is a Set?
# Python Set is a collection of unordered, unique elements.
# Similar to JavaScript Set: it removes duplicates and doesn’t maintain order.

# # Python
# my_set = {1, 2, 3, 2, 1}
# print(my_set)  # Output: {1, 2, 3}
# ✅ 2. Access Set Items
# Python sets don’t support indexing.
# Use a loop to access.
# for item in my_set:
#     print(item)
# ✅ 3. Add Items to a Set
# # Python
# my_set.add(4)
# mySet.add(4);
# ✅ 4. Remove Items from a Set
# 🔸 Python
# my_set.remove(2)     # ❌ throws error if not found
# my_set.discard(5)    # ✅ does nothing if not found
# ✅ 5. Loop Through a Set
# for item in my_set:
#     print(item)
# ✅ 6. Important Set Methods in Python
# Method	          Description	JS Equivalent
# add(x)	          Adds item	add(x)
# remove(x)	          Removes item (error if not present)	delete(x)
# discard(x)	      Removes item (no error if not present)	—
# clear()	          Removes all items	clear()
# copy()	          Returns a shallow copy	No direct equivalent
# union(set2)	      Combines two sets (like OR)	new Set([...a, ...b])
# intersection(set2)  Common items in both sets	Manual logic
# difference(set2)	  Items in set1 not in set2	Manual logic
# update(set2)	      Adds items from another set	a = new Set([...a, ...b])

# Example:
# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a.union(b))         # {1, 2, 3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a.difference(b))    # {1, 2}