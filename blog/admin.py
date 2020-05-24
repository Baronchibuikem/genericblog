from django.contrib import admin
from .models import Post, Comment, Subscription, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author',)
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created',)
    list_filter = ('created', 'updated')
    search_fields = ('name', 'body')

admin.site.register(Comment, CommentAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['your_email']
admin.site.register(Subscription, SubscriptionAdmin)

admin.site.register(Category)
