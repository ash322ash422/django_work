from rest_framework import serializers
from  .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = '__all__'
        model = Author
#end class

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Book
        