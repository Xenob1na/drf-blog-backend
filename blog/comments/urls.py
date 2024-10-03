from django.urls import path
from .views import CommentsListAPIView, DeleteCommentAPIView, CreateCommentAPIView

urlpatterns = [
    path('AllCommentsList/', CommentsListAPIView.as_view(), name="comments_list"),
    path('comment_delete/<int:pk>/', DeleteCommentAPIView.as_view(), name="delete_comment"),
    path('create_comment/', CreateCommentAPIView.as_view(), name="create_comment"),
    
]