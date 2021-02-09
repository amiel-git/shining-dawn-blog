from django.urls import path
from post.views import (PostCreateView, PostDetailView, PostListView, 
                        PostUpdateView, PostDeleteView, PublishView,
                        MyDraftsView,MyPostsView)

from django.contrib.auth.decorators import login_required

app_name = 'post'

urlpatterns = [
    path('new/',PostCreateView,name='create'),
    path('me/',MyPostsView,name='me'),
    path('drafts/',MyDraftsView,name='drafts'),
    path('',PostListView.as_view(),name='list'),
    path('<pk>/',PostDetailView.as_view(),name='detail'),
    path('<pk>/update/',login_required(PostUpdateView.as_view()),name='update'),
    path('<pk>/delete/',login_required(PostDeleteView.as_view()),name='delete'),
    path('<pk>/publish/',PublishView,name='publish'),
    
]
