from django.urls import path
from post.views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView, PublishView

app_name = 'post'

urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('new/',PostCreateView,name='create'),
    path('<pk>/',PostDetailView.as_view(),name='detail'),
    path('<pk>/update/',PostUpdateView.as_view(),name='update'),
    path('<pk>/delete/',PostDeleteView.as_view(),name='delete'),
    path('<pk>/publish/',PublishView,name='publish'),
]
