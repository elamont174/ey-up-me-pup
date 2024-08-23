from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((1,"1🐾"),(2,"2🐾"),(3,"3🐾"),(4,"4🐾"),(5,"5🐾"))
TYPE = ((0, "Pub"), (1, "Café"), (2, "Other"))



# Create your models here.
class Post(models.Model):
    location_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    pup_team = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pup_review_posts")
    rating = models.IntegerField(choices=RATING, default=None)
    type = models.IntegerField(choices=TYPE, default=2)
    featured_image = CloudinaryField('image', default='placeholder')
    review_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ["location_name"]

    def __str__(self):
        return f"{self.location_name}"


class Comment(models.Model):
    location = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="user_reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews_reviewer")
    your_rating = models.IntegerField(choices=RATING, default=None)
    your_review = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["approved"]

    def __str__(self):
        return f"{self.location}/{self.reviewer} Approved:{self.approved} "