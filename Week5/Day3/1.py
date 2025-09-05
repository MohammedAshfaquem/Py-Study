# Django supports three types of model inheritance, which allow you to reuse and structure your models more efficiently

# ✅ 1. Abstract Base Classes
# 🔹 What it is:
# Used to share common fields or methods across multiple models.
# No table is created for the abstract base class.

# 🔧 Usage:
# class CommonInfo(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     class Meta:
#         abstract = True

# class Student(CommonInfo):
#     name = models.CharField(max_length=100)
#     grade = models.CharField(max_length=10)

# class Teacher(CommonInfo):
#     name = models.CharField(max_length=100)
#     subject = models.CharField(max_length=50)

# 🧠 Result:
# Student and Teacher have their own tables, including the fields from CommonInfo.
# CommonInfo does not create a database table.


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'grade', 'created_At', 'updated_At')
#     readonly_fields = ('created_At', 'updated_At')
    
# @admin.register(Teacher)
# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('name','subject','created_At','updated_At')
#     readonly_fields = ('created_At', 'updated_At')
    
# in the admin.py we need to register like this

# 6. What happens if you try to register an abstract model in Django admin?

# A) It will work normally
# B) It raises an error
# C) It creates a dummy entry
# D) It shows no fields

# ✅ Correct Answer: B

# 10. When would you prefer abstract base classes over multi-table inheritance?

# A) When you need to keep tables separate
# B) When you want to reuse fields only
# C) When child needs different behavior
# D) When using admin proxies

# ✅ Correct Answer: B

# ✅ 2. Multi-Table Inheritance
# 🔹 What it is:
# Each model has its own table in the database.
# Used when you want to extend a model and retain the parent-child relationship in the database.
# it also usefull when we want one to one field relation

# 🔧 Usage:
# class Person(models.Model):
#     name = models.CharField(max_length=100)

# class Student(Person):
#     grade = models.CharField(max_length=10)

# 🧠 Result:
# Two tables: person and student.
# Each Student object corresponds to a Person entry (linked by an implicit OneToOneField).

# 🔄 Join Queries:
# Django will do an automatic SQL JOIN to fetch fields from both tables when you query Student.


# ✅ 3. Proxy Models
# 🔹 What it is:
# Inherits from an existing model but does not create a new table.
# Used to change behavior (e.g., ordering, methods) without altering the model's fields or structure.

# 🔧 Usage:
# class Person(models.Model):
#     name = models.CharField(max_length=100)

# class PersonProxy(Person):
#     class Meta:
#         proxy = True
#         ordering = ['name']

#     def say_hello(self):
#         return f"Hello, {self.name}!"

# 🧠 Result:
# Only one table: person.
# PersonProxy acts like a subclass with its own Python behavior, but the same database table.

# 🧾 Summary Table
# Type	                New Table?	     Use Case	                                 Inheritance Style
# Abstract Base Class	    ❌	        Share common fields/methods	                class Meta: abstract = True
# Multi-Table	            ✅	        Extend a model with full DB relationship	Regular class inheritance
# Proxy Model	            ❌	        Change behavior without changing schema	    class Meta: proxy = True