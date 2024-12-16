from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.list_or_create_blog_post, name='blog_post_list'),
    path('blogposts/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
]
