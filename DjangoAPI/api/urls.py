from django.urls import path
from .views import get_posts, create_post, post_detail

urlpatterns = [
    path('post/', create_post, name="create_post"),
    path('post/<int:pk>', post_detail, name="post_detail"),
    path('posts/', get_posts, name="get_posts"),


]
