# 🔹 Permissions in DRF
# 👉 Definition:
# Authentication = “Who are you?”
# Permissions = “What are you allowed to do?”
# In DRF, permissions decide if an authenticated (or anonymous) user can access a view or not.

# ✅ Common Built-in Permissions
# Permission	    Meaning
# AllowAny	        Everyone can access (no login needed).
# IsAuthenticated	Only logged-in users can access.
# IsAdminUser	    Only admin/staff users can access.
# IsAuthenticatedOrReadOnly	Logged-in users → full access, Anonymous → only safe methods (GET, HEAD, OPTIONS).
# ✅ Example Usage
# Global (all APIs)

# In settings.py:

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
# }


# 📌 Now, every API needs login unless overridden.

# Per View
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class PublicView(APIView):
#     permission_classes = [AllowAny]   # anyone can access
#     def get(self, request):
#         return Response({"msg": "This is public"})

# class PrivateView(APIView):
#     permission_classes = [IsAuthenticated]   # only logged-in users
#     def get(self, request):
#         return Response({"msg": f"Hello {request.user.username}"})

# ✅ Custom Permission

# Sometimes you need rules like “Only authors can edit their own posts”.
# You can create your own permission class.

# from rest_framework.permissions import BasePermission

# class IsAuthor(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.user


# Use it in a view:

# class PostDetailView(APIView):
#     permission_classes = [IsAuthor]

# ⚖️ Comparison with Django
# Feature	Django	DRF
# Authentication	Session-based login (browser)	Supports multiple (Session, Token, JWT)
# Permissions	Usually decorators (@login_required, @user_passes_test)	Built-in classes + custom permissions

# 📌 Think of it like a building 🏢
# Authentication = Security guard checks your ID → ✅ You are Ashfaque.
# Permissions = Guard checks if you can enter the library or only the lobby.