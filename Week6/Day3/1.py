# 🔹 Nested & Relational Serializers
# 👉 Serializers in DRF can also handle relationships (ForeignKey, OneToOne, ManyToMany).

# ✅ 1. Foreign Key with depth
# If our model has a foreign key, we can show related data easily using depth.
# depth=1 → shows one level of related object.
# it define inside meta class

# Example
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey("Author", on_delete=models.CASCADE)

# class Author(models.Model):
#     name = models.CharField(max_length=100)

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"
#         depth = 1   # automatically expand Author object


# 👉 Output:

# {
#   "id": 1,
#   "title": "Django for Beginners",
#   "author": {
#     "id": 2,
#     "name": "John Doe"
#   }
# }

# ✅ 2. Nested Serializer
# Instead of just depth, you can fully control by nesting another serializer.

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ["id", "name"]

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()   # nested serializer

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author"]


# 👉 Output (same as before but more customizable).

# ✅ 3. SlugRelatedField
# Show related object with a specific field instead of whole object.

# class BookSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True,
#         slug_field="name"   # show only Author name
#     )

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author"]


# 👉 Output:

# {
#   "id": 1,
#   "title": "Django for Beginners",
#   "author": "John Doe"
# }

# ⚖️ Comparison
# Method      	    Output format	                        Use case
# depth=1	        Expands related object automatically	Quick & simple
# Nested Serializer	Full control (custom fields)	        When you need customization
# SlugRelatedField	Only one field (e.g., name/email)	    When you want a short reference

# 📌 Shortcut rule:
# Small project → depth
# Need custom output → Nested serializer
# Only one field → SlugRelatedField