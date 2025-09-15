# 🔹 Authentication in DRF

# 👉 Definition:
# Authentication is the process of verifying the user’s identity before giving access to the API.
# Django: normally works with session & cookies.
# DRF: supports multiple authentication methods (tokens, JWT, sessions, etc.).

# ✅ Common Authentication Methods in DRF
# Method	             How it works	                                                                                        Example Use
# SessionAuthentication	 Uses Django sessions (like normal web login with cookies).         	                                Useful if frontend is Django templates.
# BasicAuthentication	 Username & password sent with every request (base64 encoded).	                                        Testing/simple APIs. Not secure for production without HTTPS.
# TokenAuthentication	 User gets a unique token after login → send token with every request (Authorization: Token abc123).	Mobile apps, API-only projects.
# JWT (JSON Web Token)	 User logs in → gets JWT token → send it with each request (Authorization: Bearer <token>).	            Modern APIs, SPAs (React, Angular, Vue).


# ✅ Example in DRF (Token Authentication)
# Enable in settings.py

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework.authentication.TokenAuthentication',
#     ],
# }


# Generate token for a user
# python manage.py drf_create_token <username>

# Send API request with token

# GET /students/
# Authorization: Token abc123xyz

# ✅ Example with APIView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# class ProfileView(APIView):
#     permission_classes = [IsAuthenticated]   # only logged-in users

#     def get(self, request):
#         return Response({"user": request.user.username})


# 📌 If user is not authenticated → DRF automatically returns:

# {"detail": "Authentication credentials were not provided."}


# with status 401 Unauthorized.

# ⚖️ Comparison with Django
# Feature	        Django (Web)	    DRF (API)
# Authentication	Sessions + cookies	Sessions, Basic, Token, JWT
# Usage	Browser     login/logout	    API clients, mobile apps
# Credentials	    Stored in cookies	Sent in headers (Authorization)

# 📌 Think of Authentication like a movie ticket 🎟️
# SessionAuth = Season pass (cookie stays until you log out).
# TokenAuth = Show ticket (one fixed token, reused).
# JWT = QR code ticket (self-contained, can expire/refresh).

added