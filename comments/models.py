from django.db import models
from post.models import Post
from django.contrib.auth.models import User

class Comment(models.Model):

    content = models.CharField(max_length=1000)
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        User,
        related_name = 'comments',
        on_delete = models.CASCADE
    )

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.id} {self.id}"

    
    