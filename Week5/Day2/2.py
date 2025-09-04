# 🔹 1. values()

# Returns a QuerySet of dictionaries.
# Each dictionary has field names as keys and field values as values.

# Example:
# users = User.objects.values('id', 'name')

# 👉 Output:

# <QuerySet [
#     {'id': 1, 'name': 'John'},
#     {'id': 2, 'name': 'Alice'},
#     {'id': 3, 'name': 'Bob'}
# ]>

# ✅ Useful when you want to work with data in dict form (e.g., JSON responses, APIs).

# 🔹 2. values_list()

# Returns a QuerySet of tuples.

# Each tuple contains only the field values (no keys).

# Example:
# users = User.objects.values_list('id', 'name')


# 👉 Output:

# <QuerySet [
#     (1, 'John'),
#     (2, 'Alice'),
#     (3, 'Bob')
# ]>


# ✅ More lightweight than values().

# 🔹 With flat=True
# If you select only one field, you can flatten the result into a simple list instead of tuples.
# users = User.objects.values_list('name', flat=True)


# 👉 Output:

# <QuerySet ['John', 'Alice', 'Bob']>

# 🔹 Key Differences
# Feature	        values()	                 values_list()
# Return type	    QuerySet of dicts	         QuerySet of tuples
# Keys included?	✅ Yes (field names)	       ❌ No (just values)
# Example output	{'id': 1, 'name': 'John'}	(1, 'John')
# Flat option	    ❌ Not available	           ✅ flat=True (only for single field)


# 🔹 Real Use Case
# values() → When sending data to API/JSON.
# values_list() → When you only need a list of values (e.g., for dropdowns, choices).

# ✅ Think like this:
# values() = dicts (key + value)
# values_list() = tuples (just values