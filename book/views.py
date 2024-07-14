from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from . Serializers import *


class BookViews(APIView): 
    def get(self, request):
        genre = Genre.objects.all()
        serializers = {}
        for gen in genre:
            book = Book.objects.filter(genres=gen)
            ser = BookSerializer(book,many=True)
            serializers['genre'] = ser.data
        return Response({'status':200,'payload':serializers})
    
class BookDetails(APIView):
    
    def get(self,request,id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({'status': 404, 'message': 'Book not found'})
        
        serializer = BookSerializer(book)
        return Response({'status':200,'payload':serializer.data})
