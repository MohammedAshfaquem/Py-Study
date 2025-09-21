# from rest_framework import serializers
# from .models import Book


# class BookSerializer(serializers.ModelSerializer):
#     title = serializers.SerializerMethodField()
    
#     class Meta:
#         model = Book
#         fields = '__all__'
        
    
#     def get_title(self,obj):
#         return obj.title.upper()
    
#     def validate_title(self,value):
#         if len(value) < 5:
#             raise serializers.ValidationError("Title must be at least 5 characters long.")
#         return value  
    
#     def validate(self,attrs):
#         if attrs['title'] == attrs['author']:
#             raise serializers.ValidationError("Both Are Same")
#         return attrs     
    

       
            
        
# class TestSerializer(serializers.Serializer):
    
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(read_only=True,)
    
#     def validate_title(self,value):
#         if len(value) > 5:
#             raise serializers.ValidationError("Failed")
#         return value
    