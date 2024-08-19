from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('location_name', 'slug', 'status')
    search_fields = ['location_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('location_name',)}
    summernote_fields = ('review_content',)

# Register your models here.

