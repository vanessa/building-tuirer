# URLs de tuites
from django.urls import path
from tuites.views import PostTuiteView, LikeTuiteView

app_name = 'tuites'

urlpatterns = [
    path('postar/', PostTuiteView.as_view(), name='post_tuite'),
    path('like/<int:pk>/', LikeTuiteView.as_view(), name='like'),
]