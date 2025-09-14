# 🔹 1. APIView
# Base class for building APIs.
# You write methods manually (get, post, put, delete).
# it Gives full control but more code.


# Example:

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Post
# from .serializers import PostSerializer

# class PostAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# 👉 Pros: Full control.
# 👉 Cons: More code (you write each method).



# 🔹 2. ViewSet
# A shortcut for APIs.
# You don’t write get() or post() — instead, DRF auto-generates actions like:
# .list() (GET all)
# .retrieve() (GET one)
# .create() (POST)
# .update() (PUT/PATCH)
# .destroy() (DELETE)

# Example:
# from rest_framework import viewsets

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# 👉 Then in urls.py you just use a router:

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('posts', PostViewSet)
# urlpatterns = router.urls


# 👉 API endpoints auto-created:
# GET /posts/ → list
# POST /posts/ → create
# GET /posts/1/ → retrieve
# PUT /posts/1/ → update
# DELETE /posts/1/ → destroy

# 👉 Pros: Less code, faster.
# 👉 Cons: Less flexibility (you follow DRF’s structure)


# 🔹 3. Mixins
# Small reusable classes that give specific CRUD functionality.
# You combine them to create your API.

# Example:
# from rest_framework import generics, mixins

# class PostListCreateView(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# 👉 Instead of writing everything, we mix in only what we need.
# 👉 Example mixins:

# ListModelMixin → GET all
# CreateModelMixin → POST
# RetrieveModelMixin → GET one
# UpdateModelMixin → PUT/PATCH
# DestroyModelMixin → DELETE

# ⚖️ Comparison Table
# Feature	APIView	ViewSet	Mixins
# Code	More (manual)	Less (auto)	Medium (combine pieces)
# Control	Full control	Less (auto-actions)	Balanced
# Use Case	Custom logic APIs	Quick CRUD APIs	When you need some CRUD, not all

# 📌 Think of it like building a car 🚗:
# APIView = Build from scratch (you choose every part).
# Mixins = Buy parts (engine, wheels) and assemble.
# ViewSet = Buy a ready-made car (just start driving).