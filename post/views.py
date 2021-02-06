from django.shortcuts import render
from django.views import generic
from post.models import Post
from post.forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required

class PostListView(generic.ListView):

    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


@login_required(login_url='login')
def PostCreateView(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user

            if "featured_image" in request.FILES:
                post.featured_image = request.FILES.get('featured_image')
                post.save()
                return HttpResponseRedirect(reverse('post:list'))
            else:
                post.save()
                return HttpResponseRedirect(reverse('post:list'))
        else:
            return HttpResponse(form.errors)
    
    return render(request,'post/create_post.html',context={'form':form})


class PostDetailView(generic.DetailView):

    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post_detail'