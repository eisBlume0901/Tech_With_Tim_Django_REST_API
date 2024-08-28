# Serializer converts data types (like querysets) into python data types (like dictionaries) that can be easily rendered into JSON or XML or other content types.
# query sets -> dictionaries -> JSON/XML

from rest_framework import serializers
from .models import *

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']

