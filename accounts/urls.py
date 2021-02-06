from accounts import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('register/',views.UserRegistration,name='register')
]
