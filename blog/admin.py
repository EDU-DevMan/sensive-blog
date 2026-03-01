from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'tags', 'likes')

    list_display = ('title', 'author', 'published_at')


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author')
    list_display = ('post', 'author', 'published_at')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('title',)
