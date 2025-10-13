# What are Dynamic URLs in Django?
# Static URL: Always the same for everyone (e.g., /about/)
# Dynamic URL: Changes based on data or user input (e.g., /products/5/ or /user/john/)
# In Django, we use path converters to capture part of the URL and send it to the view function as a parameter.

# Simple Example:
# 1️⃣ URL Configuration (urls.py)
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('greet/<str:name>/', views.greet_user),  
#     path('post/<int:id>/', views.show_post),      
# ]
# <str:name> → captures a string from the URL and passes it to the view.

# <int:id> → captures an integer from the URL.

# 2️⃣ Views (views.py)
# from django.http import HttpResponse

# def greet_user(request, name):
#     return HttpResponse(f"Hello, {name}!")

# def show_post(request, id):
#     return HttpResponse(f"Showing post number {id}")
# 3️⃣ How it works:
# Visiting:
# http://127.0.0.1:8000/greet/John/
# Output:
# Hello, John!
# Visiting:
# http://127.0.0.1:8000/post/10/
# Output:
# Showing post number 10
# ✅ Why useful?
# Dynamic URLs let you make pages for different data without creating separate routes for each one.
# Example: /product/1/, /product/2/, /product/3/ → all handled by one view.

# path converters:
#     str.
#     int.
#     slug:support number text underscore .
#     uuid:16 digit uniqueid.
#     path:strin with slashes.