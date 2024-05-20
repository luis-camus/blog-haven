from django.db import models

# Create your models here.
from django.contrib.auth.models import User  # If you want to associate posts with users

class BlogPost(models.Model):
    """Model representing a blog post."""
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate posts with users
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title