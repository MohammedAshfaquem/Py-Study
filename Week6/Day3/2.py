# 🔹 Serializer Customization
# 👉 DRF serializers are flexible → you can add custom fields, make fields read-only, or extra  behavior using extra_kwargs.

# ✅ 1. SerializerMethodField
# Used when you want a custom field that doesn’t exist in the model.
# Value comes from a method inside the serializer.

# class BookSerializer(serializers.ModelSerializer):
#     author_name = serializers.SerializerMethodField()

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author_name"]

#     def get_author_name(self, obj):
#         return obj.author.name   # custom logic


# 👉 Output:

# {
#   "id": 1,
#   "title": "Django for Beginners",
#   "author_name": "John Doe"
# }

# ✅ 2. read_only=True
# Makes a field non-editable.
# It will appear in output (GET), but ignored in input (POST/PUT).

# class BookSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)

#     class Meta:
#         model = Book
#         fields = ["id", "title", "author"]

# 👉 Means: user cannot send id, it will be generated automatically.

# ✅ 3. extra_kwargs
# Shortcut to customize multiple field options (like read_only, required, write_only) in one place.

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ["id", "title", "author", "created_at"]
#         extra_kwargs = {
#             "id": {"read_only": True},
#             "created_at": {"read_only": True},
#             "title": {"required": True}
#         }


# 👉 Cleaner than repeating serializers.Field(...) for every field.

# ⚖️ Key Points
# Feature	                Purpose
# SerializerMethodField	Add a custom-calculated field
# read_only=True	        Field shown in response but not editable
# extra_kwargs	        Central place to tweak field options

# 📌 Shortcut memory rule:
# Need a new field → SerializerMethodField
# Field should not be edited → read_only=True
# Want to customize multiple fields quickly → extra_kwargs