from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
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
            messages.add_message(
                request, messages.SUCCESS,
                'Your pup review has been submitted for approval!🐕')

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


# ----- Editing reviews


def user_review_edit(request, slug, user_review_id):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_review = get_object_or_404(Comment, pk=user_review_id)
    user_review_form = CommentForm(data=request.POST, instance=user_review)
    if request.method == "POST":
        if user_review_form.is_valid() and user_review.reviewer == request.user:
            user_review = user_review_form.save(commit=False)
            user_review.location = post
            user_review.approved = False
            user_review.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Pup review updated!' 
                'Close this tab and refresh to see your updated review')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating pup review...')
    context = {
        "post": post,
        "user_review": user_review,
        "user_review_form": user_review_form,
    }

    return render(request, "pup_review/edit_user_reviews.html", context)


    # ----- Deleting reviews


def user_review_delete(request, slug, user_review_id):
    """
    view to delete user review
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    user_review = get_object_or_404(Comment, pk=user_review_id)

    if user_review.reviewer == request.user:
        user_review.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own reviews!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
