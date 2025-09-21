# 🔹 Complex Data Structures in DRF
# 👉 Sometimes API data isn’t just flat — it can have lists, nested objects, or require custom fields.
# DRF serializers give us tools to handle this.

# ✅ 1. Handling Lists (many=True)
# If API returns a list of objects, we tell the serializer to expect multiple.

# Example
# books = Book.objects.all()
# serializer = BookSerializer(books, many=True)


# 👉 many=True → means list of books, not just one.

# ✅ 2. Nested Objects
# Serializer can include another serializer inside (for child objects).

# Example
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ["id", "name"]

# class BookSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer()   # nested object

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author"]


# 👉 Output:

# {
#   "id": 1,
#   "title": "Django Basics",
#   "author": {
#     "id": 2,
#     "name": "John Doe"
#   }
# }

# ✅ 3. Custom Field Serialization
# You can fully control how a field looks in the response.
# Use SerializerMethodField or override to_representation.

# Example (SerializerMethodField)
# class BookSerializer(serializers.ModelSerializer):
#     author_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author_name"]

#     def get_author_name(self, obj):
#         return obj.author.name.upper()   # custom logic


# 👉 Output:

# {
#   "id": 1,
#   "title": "Django Basics",
#   "author_name": "JOHN DOE"
# }

# ⚖️ Key Points
# Feature	    Use case
# many=True	Handle list of objects
# Nested      Serializer	Handle objects inside objects
# Custom      Field Serialization	Special formatting / calculated fields