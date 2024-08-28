from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')
    published_date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.

    def __str__(self):
        return self.title
    