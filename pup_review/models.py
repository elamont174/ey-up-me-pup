from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    location_name = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="review_posts")
    review_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)