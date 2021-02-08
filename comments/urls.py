from django.urls import path

from comments import views

app_name = 'comment'

urlpatterns = [
    path('add/<post_pk>',views.CommentCreateView,name='create')
]
