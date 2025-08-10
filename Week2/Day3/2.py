# 1. What is a View?
# A View is Python code that takes a request, processes it, and returns a response (HTML, JSON, etc.).
# In Django, a view can send data to an HTML template for rendering.

# 2. What is a Template?
# A Template is an HTML file with placeholders for dynamic content.
# Django uses its template language ({{ }} for variables, {% %} for logic).

# 3. How They Work Together
# Flow:

# User request → Django calls a view.
# View → fetches/creates data.
# View → sends data to a template.
# Template → displays the data in HTML format.
# User sees the rendered HTML page.

# 4. Simple Example
# Step 1 — View (views.py)
# from django.shortcuts import render
# def about(request):
#     context = {
#         'title': 'About Us',
#         'description': 'We are the best hospital in the city.',
#         'departments': ['Cardiology', 'Neurology', 'Orthopedics']
#     }
#     return render(request, 'about.html', context)
# Step 2 — Template (templates/about.html)
# <!DOCTYPE html>
# <html>
# <head>
#     <title>{{ title }}</title>
# </head>
# <body>
#     <h1>{{ title }}</h1>
#     <p>{{ description }}</p>

#     <h2>Departments</h2>
#     <ul>
#         {% for dept in departments %}
#             <li>{{ dept }}</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>

# Step 3 — URL (urls.py)
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('about/', views.about, name='about'),
# ]
# Result
# When you go to:
# http://127.0.0.1:8000/about/
# You’ll see:
# About Us
# We are the best hospital in the city.

# Departments:
# - Cardiology
# - Neurology
# - Orthopedics
# ✅ Key Points:

# render(request, 'template.html', context) is the main function to connect views and templates.

# context is a dictionary — keys become variables inside the template.

# Templates use {{ variable }} for data and {% for %} / {% if %} for logic.