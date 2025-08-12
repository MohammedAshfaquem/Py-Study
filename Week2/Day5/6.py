# 🔹 What are Query Parameters in a URL?
# Query parameters are the key-value pairs appended to the end of a URL,
# used to send data from the client (browser) to the server.
# They appear after the ? symbol, and multiple parameters are joined by &.

# ✅ Example URL with query parameters:
# https://example.com/search/?q=django&page=2
# Here
# q=django → the user is searching for “django”
# page=2 → user wants page 2 of the results
# 🔸 How to Access Query Params in Django
# You can access query parameters using request.GET in a view.
# Example View:
# from django.http import HttpResponse

# def search(request):
#     query = request.GET.get('q')
#     page = request.GET.get('page', 1)  # default to page 1
#     return HttpResponse(f"Search term: {query}, Page: {page}")
# So if you visit:
# http://localhost:8000/search/?q=django&page=2
# It will return:
# Search term: django, Page: 2
# 🔹 Common Use Cases
# Searching (?q=term)
# Pagination (?page=2)
# Filtering (?category=books&sort=price)
# Sorting

# 🧠 Summary
# Part	Description
# ?	Starts the query string
# q=django	A key-value pair (parameter)
# &	Separates multiple parameters
# request.GET	Django’s way to access query parameters


# ✅ Why use .get() instead of request.GET['q']?
# Using .get() is safer because:
# If 'q' doesn’t exist, request.GET.get('q') returns None
# But request.GET['q'] would raise a KeyError ❌

