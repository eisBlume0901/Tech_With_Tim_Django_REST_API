from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogPostListCreate.as_view(), name='create-blog-posts'),
    path('blogs/<int:pk>/', views.BlogPostRetrievedUpdateDestroy.as_view(), name='update-delete-blog-posts'), 
    path('blogs/search', views.BlogPostList.as_view(), name='search-blog-posts'), 
]