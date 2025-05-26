from django.contrib import admin
from .models import Post
class AdminAuthor(admin.ModelAdmin):
    pass
    


admin.site.register(Post, AdminAuthor)