# from django.shortcuts import render
# from .models import CustomUser
# from rest_framework.views import APIView
# from .serializer import UserSerializer
# from rest_framework.authtoken.models import Token
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import authenticate
# from django.contrib.auth.hashers import make_password
# from rest_framework_simplejwt.tokens import RefreshToken



# class RegisterView(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = CustomUser(username=serializer.validated_data['username'])
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 },
#                 status=status.HTTP_201_CREATED,
#             )
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self,request):
#         user = CustomUser.objects.all()
#         serializer = UserSerializer(user,many=True)
#         return Response(serializer.data)
    
# class LoginView(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username,password=password)
#         if user:
#             refresh = RefreshToken.for_user(user)
#             return Response(
#                 {
#                     "refresh": str(refresh),
#                     "access": str(refresh.access_token),
#                 },
#                 status=status.HTTP_200_OK,
#             )
#         return Response("Invalid Creadential",status=status.HTTP_401_UNAUTHORIZED)

# # Create your views here.


        # 'rest_framework_simplejwt.authentication.JWTAuthentication',

