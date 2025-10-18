# 🔹 DRF Flow: Model → View → Serializer


# 1. Model (Database structure)
# it decide what data we want  store (like Django).
# Example: A blog Post model.

# from django.db import models

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
# 👉 Database table Post created.

# 2. Serializer (Convert Model ↔ JSON)
# Django uses Forms to handle HTML.
# DRF uses Serializers to handle JSON.
# Purpose:
# Convert model objects → JSON (for API response).
# Convert JSON → model objects (for saving API request data).
# Example:

# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'created_at']


# 👉 Without serializer, DRF cannot convert database data into JSON.

# 3. View (API logic)
# it is a function that Decides what to do with a request.
# In Django → views.py returns HTML.
# In DRF → views.py returns JSON.
# Example:

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer

# class PostList(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


# 👉 Gets all posts, converts them into JSON using serializer, and returns.

# ⚖️ Flow Comparison
# Step	Django Website	DRF API
# Model	Stores data in DB	Stores data in DB
# Middle Part	Form (for HTML)	Serializer (for JSON)
# View	Returns HTML page	Returns JSON response

# 📌 In short:
# Model = Your database table
# Serializer = Translator (Model ↔ JSON)
# View = API endpoint (decides what data to send/receive)

# 👉 Imagine:
# Model = Kitchen (raw food stored)
# Serializer = Chef (cooks food into eatable form = JSON)
# View = Waiter (delivers food to customer = API response)