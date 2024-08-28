from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_user_review/<int:user_review_id>',
        views.user_review_edit, name='edit_user_reviews'),
    path(
        '<slug:slug>/delete_user_review/<int:user_review_id>',
        views.user_review_delete, name='delete_user_reviews'),
]
