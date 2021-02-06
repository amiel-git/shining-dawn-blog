from django.contrib import admin
from django.urls import path,include
from accounts.views import Index

app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('accounts/',include('accounts.urls')),
]
