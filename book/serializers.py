from rest_framework import serializers
from .models import BookModel,AuthorModel,BookCategoryModel
from django.shortcuts import get_object_or_404

    
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name','fname','date_of_birth','country')

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategoryModel
        fields = ('name',)
    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('id','author','name','category','page','price')

     
            