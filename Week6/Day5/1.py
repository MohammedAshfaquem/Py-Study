# Exception Handling & Custom Responses
# instead of crashing APIs must  handle errors and give clear messages .
# DRF provides tools for this.


# 1️⃣ Using exception_handler
# DRF has a built-in exception_handler that converts exceptions → proper JSON response.
# we can override/change error output.

# 2️⃣ Customize Validation Error Output
# DRF automatically returns 400 Bad Request with details.
# we can customize error messages inside serializer.


# ✅ Summary

# exception_handler → customize global error format.
# error_messages in serializer → customize field-level validation errors.



# 1.👉 Example:
# from rest_framework.views import exception_handler
# def custom_exception_handler(exc, context):
#     # Get default response
#     response = exception_handler(exc, context)

#     if response is not None:
#         # Add custom fields
#         response.data = {
#             "status": "error",
#             "errors": response.data,
#             "status_code": response.status_code
#         }
#     return response

# 📌 Add this in settings.py:
# REST_FRAMEWORK = {
#     "EXCEPTION_HANDLER": "myapp.utils.custom_exception_handler"
# }
# Now all API errors will follow the same format.

# 2.👉 Example:
# from rest_framework import serializers

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(
#         max_length=10,
#         error_messages={
#             "blank": "Title cannot be empty",
#             "max_length": "Title is too long (max 10 chars)."
#         }
#     )
# If invalid input is sent:
# {
#   "status": "error",
#   "errors": {
#     "title": ["Title is too long (max 10 chars)."]
#   },
#   "status_code": 400
# }



