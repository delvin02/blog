from rest_framework import serializers

from .models import Category, Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        # Assign Model into ArticleSerializer class
        model = Article
        
        # Columns Field on Article Model
        fields = (
            "id",
            "title",
            "description",
            "likes",
            "is_published",
            "category",
            "created_at",
            "modified_at",
            "get_absolute_url",
            "image",
            "url"
        )