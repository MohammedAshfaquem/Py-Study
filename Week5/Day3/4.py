# 🔹 What is prefetch_related()?

# It is a QuerySet method  in django ORM.
# It used for reverse relationships and ManyToMany fields.
# Django runs two separate queries and then joins them in Python, instead of the database.

# 👉 Good for:
# Reverse ForeignKey (user.note_set.all())
# Many-to-Many fields (student.courses.all())


# 🔹 Example Models
# class User(models.Model):
#     name = models.CharField(max_length=100)

# class Note(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
#     content = models.TextField()

# 🔹 Without prefetch_related()
# users = User.objects.all()
# for user in users:
#     for note in user.notes.all():
#         print(user.name, note.content)


# 👉 What happens:
# First query: SELECT * FROM user;
# Then for each user, Django queries their notes:
# SELECT * FROM note WHERE user_id = ?;
# Repeats for every user ❌
# ⚠️ N+1 problem again → very slow if many users.

# 🔹 With prefetch_related()
# users = User.objects.prefetch_related("notes")
# for user in users:
#     for note in user.notes.all():
#         print(user.name, note.content)


# 👉 What happens now:
# Query 1: SELECT * FROM user;
# Query 2: SELECT * FROM note WHERE user_id IN (...);
# Django links notes to users in memory.
# ✅ Only 2 queries total, no matter how many users or notes.

# 🔹 When to use prefetch_related()
# Reverse ForeignKey (one-to-many) → user.notes.all()
# Many-to-Many → student.courses.all()
# Any case where you loop through related sets.

# 🔹 Difference vs select_related()
# Feature	         select_related()	            prefetch_related()
# Works with	     ForeignKey, OneToOne	        Reverse FK, ManyToMany
# Queries	         Single SQL query with JOIN	    Two queries, combined in Python
# Performance	     Faster for single objects	    Better for collections



# 🔹 Example with Many-to-Many
# class Course(models.Model):
#     title = models.CharField(max_length=100)

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     courses = models.ManyToManyField(Course)

# students = Student.objects.prefetch_related("courses")
# for student in students:
#     print(student.name, [c.title for c in student.courses.all()])


# 👉 Runs only 2 queries (all students + all courses for them), instead of one per student.

# ✅ In short:
# select_related() = JOIN (forward foreign keys).
# prefetch_related() = separate queries + Python join (reverse / many-to-many).


# select_related() reduces queries using SQL JOIN.
# prefetch_related() reduces queries using two separate queries + Python merge.

