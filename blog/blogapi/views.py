from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer
from .forms import PostForm

class ListPostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class CreatePostAPIView(APIView):
    def post(self, request):
        post = PostForm(request.data)
        
        if post.is_valid():
            posts = post.save(commit=False)
            posts.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class DeletePostAPIView(APIView):
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetailPostAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
class UpdatePostAPIView(APIView):
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.data, instance=post)
        form.save()
        return Response(status=status.HTTP_200_OK)