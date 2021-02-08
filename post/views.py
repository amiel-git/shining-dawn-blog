from django.shortcuts import render
from django.views import generic
from post.models import Post
from post.forms import PostForm

from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required

class PostListView(generic.ListView):

    model = Post
    queryset = Post.objects.filter(is_published=True)
    template_name = 'post/post_list.html'
    context_object_name = 'posts'


@login_required(login_url='login')
def PostCreateView(request,publish=None):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=True)
            post.author = request.user
            
            if "featured_image" in request.FILES:
                post.featured_image = request.FILES.get('featured_image')
                post.save()
            else:
                post.save()

            return HttpResponseRedirect(reverse_lazy('post:detail',kwargs={'pk': post.id}))

        else:
            return HttpResponse(form.errors)
    
    return render(request,'post/create_post.html',context={'form':form})

@login_required(login_url='login')
def PublishView(request,pk):
    post = Post.objects.get(pk=pk)
    if post.author == request.user:
        post.publish()
        return HttpResponseRedirect(reverse('post:detail',kwargs={'pk': post.id}))
    else:
        raise Http404("Object Not Found")
    


class PostDetailView(generic.DetailView):

    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        """
        We need to return a 404 when someone checked on a post that is not published yet
        Except if the user accessing the unpublished post is also the owner of the post
        """
        if self.request.user == context['post_detail'].author:
            return context
        else:
            if context['post_detail'].is_published != True:
                raise Http404("Post not published yet")    
            else:
                return context
            



class PostUpdateView(generic.UpdateView):

    model = Post
    template_name = 'post/create_post.html'
    form_class = PostForm

    def get_object(self,*args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise Http404("Not your post")
        else:
            return obj


class PostDeleteView(generic.DeleteView):

    model = Post
    success_url = reverse_lazy('post:list')

    def get_object(self,*args, **kwargs):
        obj = super().get_object(*args, **kwargs)
        if obj.author != self.request.user:
            raise Http404("Not your post")
        else:
            return obj
