from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response 
# Instead of using the method-based views or api_view decorator, we can use the class-based views to create a list and detail view.
from .models import *
from .serializers import *
from rest_framework.views import APIView # For creating custom API views
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # data that will be serialized which is in object form
    serializer_class = BlogPostSerializer # Instantiating the serializer class to convert the data into JSON
    # WARNING, naming variable serializer_class is important because it is a keyword that the ListCreateAPIView class uses to determine which serializer to use.
    # This is because we are overrding the ListCreateAPIView class and we need to use the name variable names that the class is expecting.

    # Overriding the delete method
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete() # So we can able to delete all the blog posts
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BlogPostRetrievedUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk" # Primary Key
    # Retrieve - fetch the lookup object from the database
    # update - edit/modify/alter the lookup object
    # delete - remove the lookup object from the database

# How to search specific blog and has the delete optionality
# http://127.0.0.1/blogs/1
# http://127.0.0.1/blogs/7

# Custom API View - Searching a blog
class BlogPostList(APIView):
 def get(self, request, format=None):

    title = request.query_params.get('title', None) # Get the title from the query parameters

    if title: # icontains = case-insensitive
        blog_posts = BlogPost.objects.filter(title__icontains=title)    
    else:
       blog_posts = BlogPost.objects.all()
    
    serializer = BlogPostSerializer(blog_posts, many=True) # Returns a list of dictionaries
    return Response(serializer.data, status=status.HTTP_200_OK) # When the request is successful, return the data and status code 200 OK
 
 # How to search the specific blog
 # Samples:
 # http://127.0.0.1:8000/blogs/search?title=How%20APIs
 # http://127.0.0.1:8000/blogs/search?title=The
 # http://127.0.0.1:8000/blogs/search?title=Digital