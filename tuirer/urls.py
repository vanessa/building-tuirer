from django.contrib import admin
from django.urls import path

from core.views import index
from tuites.views import PostTuiteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
]
