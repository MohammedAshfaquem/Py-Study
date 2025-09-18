# 🔑 Title: External API Integration
# Sometimes, your Django REST API needs to talk to another API (example: weather API, payment gateway, or Google Maps).
# This is called External API Integration.

# 1️⃣ Consuming 3rd-party APIs
# Use Python’s requests library to make HTTP calls.
# Example: calling a weather API from inside a DRF view.

# 👉 Example (inside a view):

# import requests
# from rest_framework.response import Response
# from rest_framework.views import APIView

# class WeatherAPIView(APIView):
#     def get(self, request):
#         r = requests.get("https://api.weatherapi.com/v1/current.json?key=API_KEY&q=London")
#         data = r.json()
#         return Response(data)

# 2️⃣ Token Passthrough & Headers
# Many external APIs require auth tokens or API keys.
# These are usually passed in headers.

# 👉 Example:

# headers = {
#     "Authorization": "Bearer <api_token>"
# }
# r = requests.get("https://api.example.com/data", headers=headers)


# You can also pass user’s token if your API acts as a proxy to another service.