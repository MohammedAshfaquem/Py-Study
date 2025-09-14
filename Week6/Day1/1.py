# 🔹 Django
# Purpose:it Build websites with backend logic.
# Output: Mostly HTML templates rendered for browsers.
# Use Case: A blogging site, e-commerce site, admin dashboard, etc.


# 🔹 DRF (Django REST Framework)
# Purpose: it Build API.
# That Means machine-readable data, not HTML.
# Output: JSON, XML, etc. (mostly JSON).

# Use Case: Mobile app backend, frontend (React/Angular) API, microservices.







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


# 👉 Returns JSON:

# [
#   {"id": 1, "title": "First Post"},
#   {"id": 2, "title": "Second Post"}
# ]

# ⚖️ Key Differences: Django vs DRF
# Feature	            Django	                DRF
# Output	            HTML	                JSON / API response
# Audience	            Browsers (users)	    Apps / Frontend frameworks / APIs
# Templates needed	    ✅ Yes	              ❌ No
# Typical use	        Full-stack websites	    Backend APIs for apps or SPAs