from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "pup_review/index.html"
    paginate_by = 6

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_reviews = post.user_reviews.all().order_by("-created_on")
    user_review_count = post.user_reviews.filter(approved=True).count()

    return render(
        request,
        "pup_review/post_detail.html",
        {
            "post": post,
            "user_reviews": user_reviews,
            "user_review_count": user_review_count,
        },
    )

# ----- Editing posts

