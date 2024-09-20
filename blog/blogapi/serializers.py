from rest_framework.serializers import ModelSerializer

from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "image", "created_at"]
        
class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body", "description", "image", "created_at", "updated_at"]