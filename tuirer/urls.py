from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import index
from tuites.views import PostTuiteView
from users.views import ProfileView, ProfileEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
    
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
