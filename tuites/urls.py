# URLs de tuites
from django.urls import path
from tuites.views import PostTuiteView

app_name = 'tuites'

urlpatterns = [
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
]