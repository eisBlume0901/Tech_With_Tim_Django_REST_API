from django.shortcuts import render
from rest_framework import generics 
# Instead of using the method-based views or api_view decorator, we can use the class-based views to create a list and detail view.
from .models import *
from .serializers import *
# Create your views here.

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all() # data that will be serialized which is in object form
    serializer_class = BlogPostSerializer # Instantiating the serializer class to convert the data into JSON
    # WARNING, naming variable serializer_class is important because it is a keyword that the ListCreateAPIView class uses to determine which serializer to use.
    

