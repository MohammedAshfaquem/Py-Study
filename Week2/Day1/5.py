# 🔗 1. URL Routing (urls.py)
# What it is:
# Django uses the urls.py file to define how web addresses (URLs) are mapped to specific functions or pages in your application.

# How it works:
# When a user visits a URL, Django checks urls.py to figure out which view should handle that request.

# Example:
# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('home/', views.home, name='home'),
# ]
# In this example:
# Visiting /home/ will call the home function in views.py.



# 🧱 2. Models (models.py)
# What it is:
# Models define your database structure. Each model represents a table, and each attribute is a field in that table.
# Example:
# # models.py
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
# What it does:
# Creates a Product table in the database
# You can now add, update, delete, or query products using Django’s ORM
# After defining models:
# Run python manage.py makemigrations
# Then python manage.py migrate to apply changes to the database.




# 🎨 3. Templates (.html files)
# What it is:
# Templates are HTML files used to display content to users. Django templates can include variables
# and logic like loops and conditionals.

# Example (home.html):
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Homepage</title>
# </head>
# <body>
#     <h1>Hello, {{ username }}!</h1>
# </body>
# </html>
# Used in a view:
# def home(request):
#     return render(request, 'home.html', {'username': 'John'})
# What it does:
# The variable {{ username }} will be replaced by “John” in the browser.

# 🧠 4. Views (views.py)
# What it is:
# Views are Python functions (or classes) that handle requests and return responses.
# Typical job of a view:
# Fetch data from the database
# Render a template
# Return HTML or JSON data

# Example:
# # views.py
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the homepage!")
# Or using a template:
# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')