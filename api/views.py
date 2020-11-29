# from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User 
from .models import Article
from .serializers import ArticleSerializer, UserSerializer

# Create your views here.
class ArticleView(viewsets.ModelViewSet): 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer 

class UserView(viewsets.ModelViewSet): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]