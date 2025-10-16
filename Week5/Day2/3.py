# 🔹 What is an F object?
# Useful when you want to compare a field to another field or update a field based on its current value.

# To achieve That we need To Import:
# from django.db.models import F

# 🔹 Examples
# 1. Compare two fields
# # Get users where name length = age (just a silly example)
# User.objects.filter(age=F('id'))
# 👉 SQL:
# WHERE age = id

# 2. Field-to-field comparison
# # Users whose age is greater than their id
# User.objects.filter(age__gt=F('id'))
# 👉 SQL:
# WHERE age > id

# 3. Updating with F (no Python fetch needed)
# # Increase every user’s age by 1
# User.objects.update(age=F('age') + 1)
# 👉 This happens in the database itself (no loop in Python).

# 4. Arithmetic with F
# # Double all user ages
# User.objects.update(age=F('age') * 2)

# 5. Use with other fields
# Suppose Note model:
# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)

# # Notes where likes > views
# Note.objects.filter(likes__gt=F('views'))

# 🔹 Key Points
# ✅ Q → for complex conditions (AND, OR, NOT)
# ✅ F → for field-to-field comparisons & updates
# ✅ Runs directly in SQL → more efficient than fetching data into Python and looping.

# 🔹 SQL Mapping
# User.objects.filter(age=F('id'))
# Django generates:
# SELECT * FROM user WHERE age = id;
# ✅ Think like this:
# Q = logic between conditions
# F = reference another field in DB
