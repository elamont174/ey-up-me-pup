from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('location_name', 'review_tagline', 'type')
    search_fields = ['location_name']
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('review_tagline',)}
    summernote_fields = ('review_content',)

# Register your models here.

