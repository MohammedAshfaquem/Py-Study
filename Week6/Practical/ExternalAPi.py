# from rest_framework.views import APIView
# import requests
# from rest_framework.response import Response


# class ExternalAPIExample(APIView):
#     def get(self, request):
#         # Example: fetch random user from external API
#         url = "https://jsonplaceholder.typicode.com/users/1"
        
#         response = requests.get(url)
#         data = response.json()
        
#         return Response({
#             "message": "Fetched data from external API",
#             "data": data
#         })
        
# class TokenPassthroughView(APIView):
#     def get(self, request):
#         url = "https://api.example.com/protected/data"
#         headers = {"Authorization": request.headers.get("Authorization")}
#         response = requests.get(url, headers=headers)
#         data = response.json()
#         return Response({'data':data})