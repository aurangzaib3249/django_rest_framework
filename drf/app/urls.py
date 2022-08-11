
from django.urls import include, re_path,path

from django.contrib.auth import *

from .views import *

urlpatterns = [
    re_path(r'^$', home, name='home'),
    path('user-login/', login, name='ulogin'),
    re_path(r'^login/$', login, name='login'),
    path('logout/', logout_user, name='logout'),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
   
]