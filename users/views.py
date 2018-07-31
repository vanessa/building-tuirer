from django.views.generic import DetailView, UpdateView
from users.models import User
from django.urls import reverse_lazy
from users.mixins import ProfileAccessMixin


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile'


class ProfileEditView(ProfileAccessMixin, UpdateView):
    model = User
    fields = ('picture', 'username')
    template_name = 'profile_edit.html'
    
    def get_success_url(self):
        return reverse_lazy('profile', args=[self.object.pk])
