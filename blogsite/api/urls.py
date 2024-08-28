from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogPostListCreate.as_view(), name='create-blog-posts'),

]