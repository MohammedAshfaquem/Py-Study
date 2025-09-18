# 🔹 File Upload & Media Handling in DRF
# DRF makes it easy to upload and serve images/files through APIs.
# here Files are saved in our server’s MEDIA_ROOT.

# ✅ 1. STore Images/Files via API
# Model
# from django.db import models

# class Document(models.Model):
#     title = models.CharField(max_length=100)
#     file = models.FileField(upload_to="documents/")   # file will be saved inside MEDIA_ROOT/documents/

# Serializer
# from rest_framework import serializers
# from .models import Document

# class DocumentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ["id", "title", "file"]

# View
# from rest_framework.viewsets import ModelViewSet
# from .models import Document
# from .serializers import DocumentSerializer

# class DocumentViewSet(ModelViewSet):
#     queryset = Document.objects.all()
#     serializer_class = DocumentSerializer


# 👉 When you POST a file in Postman or frontend form, it will be uploaded.

# ✅ 2. Store Using MEDIA_ROOT
# settings.py
# import os

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# urls.py
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # your API urls here
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 👉 In development, uploaded files will be served at:

# http://127.0.0.1:8000/media/documents/yourfile.pdf

# ⚖️ Key Points
# Step	                    Purpose
# FileField / ImageField	Define where files go
# MEDIA_ROOT	            Folder where files are saved
# MEDIA_URL	                Public URL path for files
# urls.py + static()	    Serve files in development