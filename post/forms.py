from django import forms
from post.models import Post

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = [
            'title',
            'content',
            'featured_image',
        ]

        widgets = {
            'title':forms.TextInput(attrs={'type':'text','class':'post-title'}),
        }