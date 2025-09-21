# from rest_framework.generics import ListAPIView
# from rest_framework.filters import SearchFilter, OrderingFilter
# class BookListView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     filter_backends = [SearchFilter, OrderingFilter]
#     search_fields =   ['bookname', 'author__username']  # use __username to search author
#     ordering_fields = ['bookname']