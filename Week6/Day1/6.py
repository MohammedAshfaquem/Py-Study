# # 🔹 1. Request
# # In Django → request usually comes from a browser (with HTML forms, query params).
# # In DRF → request is an API call (mostly JSON).
# # DRF gives a wrapper rest_framework.request.Request which is more powerful than Django’s HttpRequest.

# # 👉 Example:

# # from rest_framework.views import APIView

# # class HelloView(APIView):
# #     def post(self, request):
# #         name = request.data.get("name")   # JSON body
# #         return Response({"message": f"Hello {name}"})


# # 📌 request.data → gets JSON body (POST, PUT, PATCH).
# # 📌 request.query_params → gets query string (?page=2).

# # 🔹 2. Response
# # In Django → response is usually HTML (via render()).
# # In DRF → response is usually JSON (via Response).
# # DRF provides rest_framework.response.Response to handle this.

# # 👉 Example:
# # from rest_framework.response import Response
# # return Response({"status": "success", "data": serializer.data})

# # 📌 Automatically converts Python dict → JSON.


# 🔹 3. Status Codes
# APIs always return a status code to tell the client what happened.
# DRF provides them in rest_framework.status module.

# 👉 Common ones:
# Code	Meaning	When used
# 200 OK	Success	Data fetched
# 201 Created	New resource created	After POST
# 400 Bad Request	Invalid input	Wrong data
# 401 Unauthorized	User not logged in	Missing auth
# 403 Forbidden	User logged in but no permission	No access rights
# 404 Not Found	Resource missing	Wrong ID
# 500 Server Error	Something broke in server	Bug

# 👉 Example:
# from rest_framework import status
# return Response({"error": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

# ⚖️ Comparison with Django
# Feature	Django (normal web)	DRF (API)
# Request	HttpRequest (form, GET/POST dicts)	Request (JSON, query params)
# Response	HttpResponse (HTML/text)	Response (JSON/dict auto-converted)
# Status	Not used much (defaults to 200)	Very important (used in every API)