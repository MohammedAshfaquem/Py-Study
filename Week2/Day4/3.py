# 🧩 Django Models (Overview)
# Definition:
# Models in Django define the structure of your database tables using Python classes.
# Each model maps to a single table in the database, and each attribute of the model represents a column in that table.

# 🔹 Basic Example
# from django.db import models

# class Person(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
# This creates a table in the database (usually called appname_person) with the following columns:
# id (automatically added by Django as the primary key)
# name (a text column with a max length of 100)
# age (an integer column)

# 🔸 How Django uses models:
# Django models handle:

# Creating tables in the database (makemigrations and migrate)
# Performing queries (e.g., filtering, creating, deleting records)
# Defining relationships (e.g., one-to-many, many-to-many)

# 🔹 Creating and using records:
# ✅ Add data
# person = Person(name='John', age=30)
# person.save()  # Saves to the database
# ✅ Read data
# person = Person.objects.get(id=1)
# print(person.name)
# ✅ Update data
# person.age = 31
# person.save()
# ✅ Delete data
# person.delete()
# 🔹 Common Field Types:
# Field Type	Description
# CharField	Text field with max length
# TextField	Long text field
# IntegerField	Whole numbers
# BooleanField	True/False
# DateField	Date only
# DateTimeField	Date and time
# ForeignKey	One-to-many relationship
# ManyToManyField	Many-to-many relationship

# 🔹 How to apply model changes:
# Create migration (detects changes in models):
# python manage.py makemigrations
# Apply migration (creates/updates database tables):
# python manage.py migrate
# 🔹 Admin Integration:
# If you register your model in the Django admin, you can manage it from the admin panel:
# from django.contrib import admin
# from .models import Person

# admin.site.register(Person)