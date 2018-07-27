from django.contrib import admin
from django.urls import path
from core.views import index

from tuites.views import post_tuite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('postar/', post_tuite, name='post_tuite'),
]