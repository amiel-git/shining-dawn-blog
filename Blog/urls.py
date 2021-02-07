from django.contrib import admin
from django.urls import path,include
from accounts.views import index,loginview,logoutview

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login/',loginview,name='login'),
    path('logout/',logoutview,name='logout'),
    path('accounts/',include('accounts.urls')),
    path('posts/',include('post.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
