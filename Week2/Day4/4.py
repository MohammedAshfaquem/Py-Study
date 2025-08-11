# Great — you're asking how to build a login/logout system in Django using:

# ✅ Django's inbuilt User model
# ✅ No custom forms.py
# ✅ Using functions: authenticate(), login(), logout()
# ✅ Protecting views with @login_required

# I'll walk you through the full working setup step-by-step.
# ✅ Step-by-Step Guide: Login Project in Django
# 1. Create Django Project and App
# django-admin startproject loginproject
# cd loginproject
# python manage.py startapp accounts
# 2. Update settings.py
# In loginproject/settings.py:
# INSTALLED_APPS = [
#     ...
#     'accounts',  # your app
#     'django.contrib.auth',
#     'django.contrib.sessions',
# ]

# # For redirecting after login/logout
# LOGIN_URL = '/login/'             # where to redirect if user not logged in
# LOGIN_REDIRECT_URL = '/'          # where to go after login
# LOGOUT_REDIRECT_URL = '/login/'  # where to go after logout
# 3. Create URL patterns
# loginproject/urls.py:
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('accounts.urls')),
# ]
# accounts/urls.py:
# Create this file if it doesn't exist.

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]
# 4. Create Views Using authenticate(), login(), logout()
# accounts/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, 'login.html')

# def user_logout(request):
#     logout(request)
#     return redirect('login')

# @login_required
# def home(request):
#     return render(request, 'home.html', {'user': request.user})
# 5. Create Templates
# Create a templates folder inside your accounts app and add these files:

# accounts/templates/login.html
# <h2>Login</h2>
# <form method="post">
#     {% csrf_token %}
#     <input type="text" name="username" placeholder="Username"><br>
#     <input type="password" name="password" placeholder="Password"><br>
#     <button type="submit">Login</button>
# </form>
# {% if messages %}
#   {% for message in messages %}
#     <p style="color: red">{{ message }}</p>
#   {% endfor %}
# {% endif %}
# accounts/templates/home.html
# <h2>Welcome, {{ user.username }}</h2>
# <a href="{% url 'logout' %}">Logout</a>
# 6. Migrate and Create Superuser
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# 7. Run the Server
# python manage.py runserver
# Visit:
# http://127.0.0.1:8000/login/ – to log in
# http://127.0.0.1:8000/ – home page (protected by login)
# http://127.0.0.1:8000/logout/ – to log out

# 🔐 Explanation of Functions
# Function	Purpose
# authenticate()	    Verifies username and password, returns User object or None
# login(request, user)	Logs the user in and starts the session
# logout(request)	    Ends the session and logs out the user
# @login_required	    Restricts view access to authenticated users only