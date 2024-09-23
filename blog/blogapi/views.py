from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import Post, Category
from .serializers import PostSerializer, PostDetailSerializer, CategorySerializer
from .forms import PostForm

class ListPostAPIView(APIView):
    def get(self, request):
        category_query = request.GET.get('category')
        if category_query:
            category = Category.objects.filter(title__icontains=category_query).first()
            if category:
                posts = Post.objects.filter(category=category)
            else:
                return Response({"message": "Такой категории не существует"}, status=status.HTTP_404_NOT_FOUND)
        elif category_query is None:
            posts = Post.objects.all()
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
class CreatePostAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):

        
        post = PostForm(request.data)
        
        if post.is_valid():
            posts = post.save(commit=False)
            posts.created_by = request.user
            posts.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class DeletePostAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk, created_by=request.user)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DetailPostAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
    
class UpdatePostAPIView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, pk):
        post = Post.objects.get(pk=pk, created_by=request.user)
        form = PostForm(request.data, instance=post)
        form.save()
        return Response(status=status.HTTP_200_OK)
    
class CategoryListAPIView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    