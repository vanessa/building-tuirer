from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import index
from tuites.views import PostTuiteView
from users.views import ProfileView, ProfileEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='profile-edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
