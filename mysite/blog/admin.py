from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    fields = ('title', 'pub_date', 'content',)
    list_display = ('title', 'pub_str', 'likes')
    list_filter = ('pub_date',)
    search_fields = ('title', 'content')