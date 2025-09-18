# 🔐 Title: Role-based Permissions
# Permissions decide what an authenticated user can do.
# Role-based permissions → give access based on user role (e.g., Admin, Staff, Regular User).
# Not all users should have the same power.
# Example:
# Admin → full CRUD
# Staff → read + update
# User → read-only

# 1️⃣ Group-based Access Control
# 👉 Useful for: assigning permissions to a set of users (instead of user-by-user).
# Django has Groups (from django.contrib.auth.models).
# Users inside a group automatically get the group’s permissions.

# 2️⃣ Built-in Permissions in DRF
# IsAuthenticated → only logged-in users.
# IsAdminUser → only admins.
# IsAuthenticatedOrReadOnly → safe methods (GET) for everyone, others need login.

# 3️⃣ Custom Role-based Permission
# 👉 Example: only staff users can edit books.

# from rest_framework.permissions import BasePermission

# class IsStaffOrReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         if request.method in ['GET', 'HEAD', 'OPTIONS']:
#             return True  # read-only for all
#         return request.user.is_staff  # write only for staff


# Use in view:

# from rest_framework.viewsets import ModelViewSet
# from .models import Book
# from .serializers import BookSerializer
# from .permissions import IsStaffOrReadOnly

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsStaffOrReadOnly]

# 4️⃣ Real-world Example
# E-commerce API:
# Admin → add/remove products.
# Seller → update own products.
# Customer → only view products.

# 📝 Key Points
# Authentication = who you are
# Permission = what you can do
# Built-in + custom classes make role-based access easy.
# Always combine with authentication for security.