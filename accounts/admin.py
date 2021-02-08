from django.contrib import admin
from accounts.models import StaffProfile,UserProfile
from post.models import Post
from comments.models import Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)