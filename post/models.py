from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse

from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    featured_image = models.ImageField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='posts',null=True)
    published_date = models.DateField(blank=True,null=True)
    created_on = models.DateField(auto_now_add=True)


    def publish(self):
        self.is_published = True
        self.published_date = timezone.now()
        self.save()
        

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

## ADD Comments Model