from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(LoginRequiredMixin, CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:post_tuite')

    def get_initial(self):
        return {
            'user': self.request.user
        }

    def form_valid(self, form):
        messages.success(
            self.request,
            'Você postou um Tuite!'
        )
        return super().form_valid(form)
