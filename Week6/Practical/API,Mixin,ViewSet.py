from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Book
from rest_framework import status,generics,mixins
from .serializers import BookSerializer,TestSerializer
from rest_framework.response import Response


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

data = []
class TestView(APIView):
    def post(self,request):
        serializer = TestSerializer(data=request.data)
        
        if serializer.is_valid():
            data.append(serializer.validated_data)
            return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        return Response(data)
    
class MixinView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    # def get(self,request):
    #     book = Book.objects.all()
    #     serializer = BookSerializer(book,many = True)
    #     return Response(serializer.data)
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs,)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs,)
    
        
    
    
    
            