# 📝 Definition
# Django View Engine refers to Django’s mechanism for processing HTTP requests, applying business logic, and returning HTTP responses.
# It connects URLs (from urls.py) to Python functions or classes that decide what the user sees.

# 💡 How It Works
# User makes a request (e.g., /home).
# urls.py matches that URL to a view function.
# The view runs your Python code → fetch data → process logic.
# The view returns:
# Raw text → HttpResponse
# Rendered HTML template → render()
# Redirect → HttpResponseRedirect

# ⚙ Common Methods
# HttpResponse() → Send plain text or HTML directly.
# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello, Django!")


# render() → Render a template with context data.
# from django.shortcuts import render
# def home_view(request):
#     return render(request, 'home.html', {'name': 'Ashfaque'})


# redirect() → Redirect to another URL.
# from django.shortcuts import redirect
# def go_to_home(request):
#     return redirect('home')


# 📌 Summary
# View = Logic layer between model (data) and template (UI).
# Can return HTML, JSON, files, or redirects.
# Uses HttpResponse, render(), redirect() to create responses.