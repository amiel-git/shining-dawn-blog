from django.shortcuts import render

from comments.models import Comment
from post.models import Post

from django.views import generic
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect,Http404
from django.urls import reverse_lazy

from Blog.utilities import has_comment_update_delete_access



def CommentCreateView(request,post_pk):
    
    if request.method == "POST":
        post = get_object_or_404(Post,pk=post_pk)
        author = request.user
        content = request.POST.get('content')

        comment = Comment(post=post,author=author,content=content)

        comment.save()

        return HttpResponseRedirect(reverse_lazy('post:detail',kwargs={'pk':post_pk}))


def CommentUpdateView(request,comment_pk,post_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)

    #Permission Check
    if has_comment_update_delete_access(comment,request.user):

        if request.method == "POST":
            comment.content = request.POST.get('content')
            comment.save()
            return HttpResponseRedirect(reverse_lazy('post:detail',kwargs={'pk':post_pk}))


def CommentDeleteView(request,comment_pk,post_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if has_comment_update_delete_access(comment,request.user):
        if request.method == "POST":
            comment.delete()
            return HttpResponseRedirect(reverse_lazy('post:detail',kwargs={'pk':post_pk}))    