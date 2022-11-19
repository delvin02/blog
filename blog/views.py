from django.shortcuts import render
from django.http import HttpResponse

# Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

# Serializer 
from .serializers import ArticleSerializer

from .models import Article, Category

# Create your views here.
class LatestArticlesList(APIView):

    # GET Latest Articles
    def get(self, request, format=None):

        # Query Article (all)
        article = Article.objects.all()
        # Converting to native python datatype that can be rendered into JSON (Serialize)
        serializer = ArticleSerializer(article, many=True)
        # Publish the data
        return Response(serializer.data)


def index(request):
    articles = Article.objects.all()
    return render(request, "blog/index.html", {
        "articles": articles
    })

def article(request):
    return render(request, "blog/article.html")

