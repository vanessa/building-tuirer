from django.urls import path
from users.views import ProfileView, ProfileEditView

# Este é o nome do namespace
app_name = 'users'

urlpatterns = [
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),  # `name` é o nome da URL
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='edit_profile'),
]

# Para chamar a URL do perfil, por exemplo, no reverse(),
# temos que passar no formato `app_name:name`, ou seja,
# para a URL do perfil => users:profile
#
# Exemplos: reverse('users:profile'), {% url 'users:profile' user.pk %}