from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('location_name', 'type')
    search_fields = ['location_name']
    list_filter = ('type',)
    prepopulated_fields = {'slug': ('location_name',)}
    summernote_fields = ('review_content',)

# Register your models here.
admin.site.register(Comment)

