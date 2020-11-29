from rest_framework import serializers 
from django.contrib.auth.models import User 
from .models import Article 

class ArticleSerializer(serializers.HyperlinkedModelSerializer): 
    class Meta: 
        model = Article 
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            "id", 
            "username", 
        )