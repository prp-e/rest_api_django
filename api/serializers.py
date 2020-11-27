from rest_framework import serializers 
from .models import Article 

class ArticleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Artilce 
        fields = '__all__'