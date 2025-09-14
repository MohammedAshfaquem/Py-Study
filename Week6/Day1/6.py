# 🔹 1. Request
# In Django → request usually comes from a browser (with HTML forms, query params).
# In DRF → request is an API call (mostly JSON).
# DRF gives a wrapper rest_framework.request.Request which is more powerful than Django’s HttpRequest.

# 👉 Example:

# from rest_framework.views import APIView

# class HelloView(APIView):
#     def post(self, request):
#         name = request.data.get("name")   # JSON body
#         return Response({"message": f"Hello {name}"})


# 📌 request.data → gets JSON body (POST, PUT, PATCH).
# 📌 request.query_params → gets query string (?page=2).

# 🔹 2. Response

# In Django → response is usually HTML (via render()).

# In DRF → response is usually JSON (via Response).

# DRF provides rest_framework.response.Response to handle this.

# 👉 Example:

# from rest_framework.response import Response

# return Response({"status": "success", "data": serializer.data})


# 📌 Automatically converts Python dict → JSON.