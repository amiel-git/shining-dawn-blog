from django.urls import path
from post.views import PostCreateView, PostDetailView, PostListView

app_name = 'post'

urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('new/',PostCreateView,name='create')
]
