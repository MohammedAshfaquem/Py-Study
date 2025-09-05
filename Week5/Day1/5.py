# 🔹 What is a Q object?
# In Django, a Q object is used to build complex queries with conditions.
# it use AND,OR and NOT logic.
# Normally, .filter() applies an AND between conditions. But with Q, you can write more flexible queries.

# 🔹 When to Use?
# When you need OR queries (|).
# When you need complex AND/OR mixes.
# When you need NOT conditions.
# When you want dynamic queries (conditions only if provided).

# 🔹 Import
# from django.db.models import Q

# 🔹 Examples
# 1. Normal filter (AND condition by default)
# # Fetch users whose name is "John" AND age is 25
# User.objects.filter(name="John", age=25)
# Equivalent to:
# WHERE name="John" AND age=25

# 2. Using Q for OR
# # Users whose name is John OR age is 25
# User.objects.filter(Q(name="John") | Q(age=25))
# Equivalent to:
# WHERE name="John" OR age=25

# 3. Using Q for AND
# # Users whose name is John AND age is 25
# User.objects.filter(Q(name="John") & Q(age=25))
# (same as normal .filter())

# 4. Using Q for NOT
# # Users whose name is NOT John
# User.objects.filter(~Q(name="John"))
# Equivalent to:
# WHERE NOT name="John"

# 5. Combining multiple
# # Users whose name is John OR (age is greater than 30 AND email contains 'gmail')
# User.objects.filter(
#     Q(name="John") | (Q(age__gt=30) & Q(email__icontains="gmail"))
# )



# dynamic query example

# from django.db.models import Q

# def search_users(name=None, age=None, email=None):
#     query = Q()  # start empty
    
#     if name:
#         query &= Q(name__icontains=name)
#     if age:
#         query &= Q(age=age)
#     if email:
#         query &= Q(email__icontains=email)

#     return User.objects.filter(query)
