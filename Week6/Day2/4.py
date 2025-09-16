# 🔹 CRUD with ModelViewSet

# 👉 What is ModelViewSet?
# Combines all the actions (list, create, retrieve, update, destroy).
# here we dont need to write seperate views for crud
# it Works with routers that  auto-generate URLs.

# ✅ Example: Book API
# 1. Serializer
# from rest_framework import serializers
# from .models import Book

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"

# 2. ViewSet
# from rest_framework.viewsets import ModelViewSet
# from .models import Book
# from .serializers import BookSerializer

# class BookViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# 3. Router (urls.py)
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)   # /books/ endpoint

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# ✅ Now You Get These Endpoints Automatically:
# HTTP Method	URL	Action
# GET	/books/	List all books
# POST	/books/	Create new book
# GET	/books/1/	Retrieve book with id=1
# PUT	/books/1/	Update book with id=1
# PATCH	/books/1/	Partial update
# DELETE	/books/1/	Delete book

# 📌 Advantage: No need to write multiple APIViews → one class + router handles everything.