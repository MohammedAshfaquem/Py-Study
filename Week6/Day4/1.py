# 🔹 Token-Based Authentication
# Instead of logging in with username & password every time, the API gives you a token after login.
# Then you send that token with every request → the API knows who you are.

# ✅ 1. Using TokenAuthentication with obtain_auth_token
# DRF provides a built-in token system(rest_framework.authtoken ).
# Each user has a unique token stored in DB.
# You can get it using obtain_auth_token.


# Setup
# settings.py

# INSTALLED_APPS = [
#     ...
#     'rest_framework.authtoken',
# ]


# urls.py

# from django.urls import path
# from rest_framework.authtoken.views import obtain_auth_token

# urlpatterns = [
#     path('api/token/', obtain_auth_token),   # login endpoint
# ]


# 👉 Example Request:

# POST /api/token/
# {
#   "username": "john",
#   "password": "1234"
# }


# 👉 Example Response:

# {
#   "token": "3fcd02a9e7a5c6..."
# }


# 👉 Then client sends token in header:
# Authorization: Token 3fcd02a9e7a5c6...

# ✅ 2. Custom Login Endpoints
# Sometimes we want to return extra data (like user info along with token).
# We can create our own login API.

# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth import authenticate

# class CustomLoginView(APIView):
#     def post(self, request):
#         user = authenticate(
#             username=request.data.get("username"),
#             password=request.data.get("password")
#         )
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({
#                 "token": token.key,
#                 "user_id": user.id,
#                 "username": user.username
#             })
#         return Response({"error": "Invalid credentials"}, status=400)


# 👉 Now you control the response format.

# ⚖️ Key Points
# Feature	    TokenAuthentication
# Storage	    Token stored in DB
# Login	        obtain_auth_token or custom view
# Header	    Authorization: Token <token>
# Good for	    Small/medium apps
# Limitation	Server checks DB for token on every request (not great for big apps)