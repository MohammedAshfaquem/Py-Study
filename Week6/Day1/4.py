# 🔹 DRF Serializers
# In Django → we use Forms to convert HTML form data ↔ Models.
# In DRF → we use Serializers to convert JSON ↔ Models.

# Purpose:
# Convert Model objects → JSON (for API response).
# Convert JSON → Model objects (for saving API request data).
# Serializer = Translator between Database and API

# 🔹 Types of Serializers in DRF
# 1. Basic Serializer
# Works like Django forms.Form.
# You manually define fields.
# Useful when we don’t have a Model (or want full control).
# Example:

# from rest_framework import serializers

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()

# 2. ModelSerializer
# Just like Django’s ModelForm.
# Automatically generates fields from a Model.
# Saves a LOT of code.
# Shortcut for serializers.


# Example:
# from rest_framework import serializers
# from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'created_at']



# ⚖️ Comparison: Forms vs Serializers
# Feature	    Django Form	    DRF Serializer
# Input	        HTML Form	    JSON Data
# Output	    HTML Page	    JSON Response
# Validation	✅ Yes	      ✅ Yes
# For Models	ModelForm	    ModelSerializer


# 🔹 1. Fields
# it like Django model fields but for APIs.
# it decide what data goes in/out.

# Example:
# from rest_framework import serializers

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True)


# 📌 Common fields:
# CharField → text
# IntegerField → numbers
# BooleanField → true/false
# DateTimeField → timestamps
# EmailField → emails
# SerializerMethodField → custom computed field

# 🔹 2. Validation
# Serializers automatically validate fields (e.g., max_length, required).
# But you can also add custom validation.

# ✅ Field-level validation
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']

#     def validate_title(self, value):
#         if "bad" in value.lower():
#             raise serializers.ValidationError("Title contains a forbidden word!")
#         return value


# 👉 If someone tries to save a Post with "bad" in title → ❌ error.
# ✅ Object-level validation
# (Validate across multiple fields together)

#     def validate(self, data):
#         if data['title'] == data['content']:
#             raise serializers.ValidationError("Title and content cannot be the same!")
#         return data

# 🔹 3. Customization
# You can customize how data is represented.

# ✅ Add extra read-only field
# class PostSerializer(serializers.ModelSerializer):
#     word_count = serializers.SerializerMethodField()

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content', 'word_count']

#     def get_word_count(self, obj):
#         return len(obj.content.split())


# 👉 API response will include word_count even though it’s not in the model.
# ✅ Control which fields show
# Show only some fields depending on the request.

# class DynamicPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'content']

#     def __init__(self, *args, **kwargs):
#         fields = kwargs.pop('fields', None)
#         super().__init__(*args, **kwargs)

#         if fields:
#             for field in set(self.fields) - set(fields):
#                 self.fields.pop(field)


# 👉 Now you can do:
# DynamicPostSerializer(post, fields=['id', 'title']) → only id & title.

# ⚖️ Summary
# Feature	Use
# Fields	Define what data is exposed in API
# Validation	Ensure incoming JSON is correct
# Customization	Add extra fields or control output