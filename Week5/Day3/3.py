# 🔹 What is select_related()?
# It is a QuerySet method in Django ORM.
# it used with  foreign key relationships and also one to one feilds
# it like SQL join
# it Mainly Used for optimization (reducing queries).
# It tells Django:
# 👉 “When you fetch this object, also fetch its related object in the same query (SQL JOIN), instead of hitting the database again.”


# Example Models
# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()

# 🔹 Without select_related()
# notes = Note.objects.all()
# for note in notes:
#     print(note.content, note.user.name)


# 👉 What happens here:
# First query: SELECT * FROM note;
# Then for each note, Django fetches its user separately:
# SELECT * FROM user WHERE id = ?;
# (Repeats for every note)
# ⚠️ Problem: This is called N+1 query problem → very inefficient if you have 100 notes.very slow if many users.

# 🔹 With select_related()
# notes = Note.objects.select_related("user")
# for note in notes:
#     print(note.content, note.user.name)


# 👉 What happens now:
# Only one SQL query:
# SELECT note.id, note.content, user.id, user.name
# FROM note
# INNER JOIN user ON note.user_id = user.id;


# Django already knows about the user, so no extra queries are made.
# ✅ Much faster for foreign key lookups.



# 🔹 When to use select_related()
# When you’re accessing ForeignKey or OneToOneField related objects.
# Example:
# Note → User
# Profile → User
# Order → Customer

# 🔹 When NOT to use
# For reverse relationships (like user.note_set.all()) or ManyToMany fields → use prefetch_related() instead.

# 🔹 Summary
# select_related() = SQL JOIN (foreign key / one-to-one).
# Reduces DB hits.
# Best for forward relationships.
# Still returns model objects, just optimized.