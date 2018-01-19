from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'published_on')
admin.site.register(Post, PostAdmin)
