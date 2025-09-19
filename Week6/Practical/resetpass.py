# from rest_framework.response import Response
# from django.contrib.auth.hashers import make_password

# class PasswordResetView(APIView):
#     def post(self,request):
#         username = request.data.get('username')
#         new_pass = request.data.get('password')
        
#         try:
#             user = CustomUser(username=username)
#             user.password = make_password(new_pass)
#             user.save()
#             return Response('Password Update Successfully',status=status.HTTP_200_OK)
#         except CustomUser.DoesNotExist:
#             return Response('User Not exist',status=status.HTTP_401_UNAUTHORIZED)