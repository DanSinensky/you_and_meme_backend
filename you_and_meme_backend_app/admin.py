from django.contrib import admin
from .models import Profile, Post, Comment, Meme

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Meme)
