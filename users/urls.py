# URLs de users
from django.urls import path

# Escolher um dos dois
from users.views import ProfileView, ProfileEditView, UserLoginView, \
                        UserLogoutView, UserSignupView

app_name = 'users'

urlpatterns = [
    path('perfil/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('perfil/<int:pk>/editar/', ProfileEditView.as_view(), name='profile-edit'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('cadastro/', UserSignupView.as_view(), name='signup'),
]