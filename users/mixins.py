from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import User
from django.shortcuts import redirect
from django.contrib import messages


class ProfileAccessMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        # Mostrando mensagens 
        messages.error(
            self.request,
            'Você não pode editar um perfil que não é seu!'
        )
        return redirect('index')

    def dispatch(self, request, *args, **kwargs):
        user_pk = kwargs.get('pk')
        user = User.objects.get(pk=user_pk)
        if not user == request.user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
