# 🔹 URL Routing in DRF
# Routing decides which URL calls which view.
# In DRF, we can set up routing in two main ways:

# ✅ 1. Using routers.DefaultRouter() (for ViewSet / ModelViewSet)
# Automatically generates CRUD URLs for you.
# Best when using ViewSets.

# Example:
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]


# 👉 This automatically gives:
# /books/ → list, create
# /books/1/ → retrieve, update, delete

# ✅ 2. Manual URL conf (for APIView)
# You write URLs one by one.
# Best when using APIView or function-based views.

# Example:
# from django.urls import path
# from .views import BookListCreateView, BookDetailView

# urlpatterns = [
#     path('books/', BookListCreateView.as_view()),   # GET, POST
#     path('books/<int:pk>/', BookDetailView.as_view()),  # GET, PUT, DELETE
# ]


# 👉 Here, you manually control each endpoint.

# ⚖️ Comparison
# Feature	Router (DefaultRouter) 🚀	Manual URL (APIView) 🛠️
# Setup	Very quick	More typing needed
# URL Generation	Automatic (CRUD ready)	You define each path
# Flexibility	Less (follows CRUD)	More (custom logic)

# 📌 Shortcut rule:
# Use Router → if using ViewSet / ModelViewSet.
# Use Manual URL → if using APIView.