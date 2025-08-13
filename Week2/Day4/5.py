# 🎯 Goal:
# ✅ Create an HTML form
# ✅ Submit it using the POST method
# ✅ Handle the submitted data in the Django view using:
# if request.method == 'POST':
# ✅ Step 1: Create the HTML Form
# Create a file named form.html inside your templates/ folder.
# <!-- templates/form.html -->
# <h2>Contact Form</h2>
# <form method="post">
#     {% csrf_token %}
#     <input type="text" name="name" placeholder="Enter your name"><br><br>
#     <input type="email" name="email" placeholder="Enter your email"><br><br>
#     <button type="submit">Submit</button>
# </form>
# 🔐 Why csrf_token?
# It protects against Cross-Site Request Forgery. Required for all POST forms in Django.

# ✅ Step 2: Create the View (Handle POST)
# In your views.py:
# from django.shortcuts import render

# def contact_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         # You can now save this data, send an email, etc.
#         print(f"Name: {name}, Email: {email}")

#         return render(request, 'form.html', {'message': 'Form submitted successfully!'})

#     return render(request, 'form.html')
# 🔍 Explanation:
# if request.method == 'POST':
# ✅ True when the form is submitted

# ✍️ You can access submitted values using:
# request.POST.get('field_name')
# ✅ Step 3: Add a URL Pattern
# In urls.py:
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('contact/', views.contact_view, name='contact'),
# ]
# ✅ Step 4: Run the Server
# python manage.py runserver
# Now go to:
# 👉 http://127.0.0.1:8000/contact/

# Fill the for
# Click submit
# The view will print the submitted data and show a success message

# ✅ Summary
# Part	What it does
# method="post"	    Sends form data securely to the server
# csrf_token	    Required for security
# if request.method == 'POST'	Checks if the form was submitted
# request.POST.get()	Retrieves submitted data from the form