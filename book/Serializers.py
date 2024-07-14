from rest_framework import serializers
from manageuser.serializers import UserSeralizer
from . models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        


class BookSerializer(serializers.ModelSerializer):
    genres = GenereSerializer()
    publisher = PublisherSerializer()
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = '__all__'

class BookInstanceSerializer(serializers.ModelSerializer):
    borrower = UserSeralizer()
    book = BookSerializer ()
    class Meta:
        model = BookInstance
        fields = '__all__'