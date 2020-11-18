from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('title',)