from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

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
    if request.method == "POST":
        user_review_form = CommentForm(data=request.POST)
        if user_review_form.is_valid():
            user_review = user_review_form.save(commit=False)
            user_review.reviewer = request.user
            user_review.location = post
            user_review.save()
            messages.add_message(request, messages.SUCCESS, 'Your pup review has been submitted for approval!🐕')

    user_review_form = CommentForm()

    return render(
        request,
        "pup_review/post_detail.html",
        {
            "post": post,
            "user_reviews": user_reviews,
            "user_review_count": user_review_count,
            "user_review_form": user_review_form,
        },
    )

# ----- Editing posts

