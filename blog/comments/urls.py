from django.urls import path
from .views import CommentsListAPIView, DeleteCommentAPIView, CreateCommentAPIView, UpdateCommentAPIView


urlpatterns = [
    path('all_comments_list/', CommentsListAPIView.as_view(), name="comments_list"),
    path('create_comment/', CreateCommentAPIView.as_view(), name="create_comment"),
    path('comment_delete/<int:pk>/', DeleteCommentAPIView.as_view(), name="delete_comment"),
    path('update_comment/<int:pk>/', UpdateCommentAPIView.as_view(), name="update_comment"),
]