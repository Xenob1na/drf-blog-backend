from rest_framework.serializers import ModelSerializer

from .models import Post, Category

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "category", "image", "created_at"]
        
class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "description", "category", "image", "created_by", "created_at", "updated_at"]
        
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]   
        