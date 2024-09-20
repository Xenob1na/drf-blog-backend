from django.urls import path
from .views import ListPostAPIView, DetailPostAPIView, DeletePostAPIView, CreatePostAPIView, UpdatePostAPIView

urlpatterns = [
    path('AllPostList/', ListPostAPIView.as_view(), name="post_list"),
    path('post_create/', CreatePostAPIView.as_view(), name="post_create"),
    path("post/<int:pk>/", DetailPostAPIView.as_view(), name="post_detail"),
    path("post_delete/<int:pk>/", DeletePostAPIView.as_view(), name="post_delete"),
    path("post_update/<int:pk>/", UpdatePostAPIView.as_view(), name="post_update"),
]