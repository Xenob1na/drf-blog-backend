from rest_framework.serializers import ModelSerializer

from .models import Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "post", "body", "created_at", "created_by"]  