# 🔹 Input Validation & Sanitization in DRF
# 👉 When clients send data to API, we must validate (check correctness) and sanitize (clean/format it).
# DRF serializers give built-in hooks for this.

# ✅ 1. Field-Level Validation (validate_<field>())
# Checks a single field.
# Method name must be validate_<fieldname>.

# Example
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ["title", "pages"]

#     def validate_pages(self, value):
#         if value <= 0:
#             raise serializers.ValidationError("Pages must be greater than 0")
#         return value


# 👉 If pages = -5, it raises an error.

# ✅ 2. Object-Level Validation (validate(self, attrs))
# Checks multiple fields together.
# Useful when validation depends on the relation between fields.

# Example
# class EventSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Event
#         fields = ["start_date", "end_date"]

#     def validate(self, attrs):
#         if attrs["end_date"] < attrs["start_date"]:
#             raise serializers.ValidationError("End date must be after start date")
#         return attrs


# 👉 Ensures event dates make sense.

# ✅ 3. Sanitization
# Sometimes we clean/format input before saving.
# Example: trimming spaces, converting to lowercase.

# def validate_title(self, value):
#     return value.strip().title()   # Clean & format

# ⚖️ Key Points
# Type	        Method	Use case
# Field-level	validate_<field>()	    Check one field
# Object-level	validate(self, attrs)	Check relation between multiple fields
# Sanitization	Inside validate methods	Clean/format input