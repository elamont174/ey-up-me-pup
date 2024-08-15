from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((1,"1🐾"),(2,"2🐾"),(3,"3🐾"),(4,"4🐾"),(5,"5🐾"))



# Create your models here.
class Post(models.Model):
    location_name = models.CharField(max_length=200, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pup_review_posts")
    rating = models.IntegerField(choices=RATING, default=None)
    review_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ["location_name"]

    def __str__(self):
        return f"{self.location_name}"