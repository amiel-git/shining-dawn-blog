from django.urls import path

from comments import views

app_name = 'comment'

urlpatterns = [
    path('add/<post_pk>',views.CommentCreateView,name='create'),
    path('<comment_pk>/update/<post_pk>/',views.CommentUpdateView,name='update'),
    path('<comment_pk>/delete/<post_pk>/',views.CommentDeleteView,name='delete'),
]
