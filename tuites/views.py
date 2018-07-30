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
    success_url = reverse_lazy('post_tuite')

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

# Código não utilizado \/

def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando formulário!')
        # print(request.POST)
        content = request.POST.get('content', None)
        if content.isspace() or content == '':
            context['error'] = 'Tuite não pode estar vazio!'
        else:
            Tuite.objects.create(
                content=content,
                author=request.user,
            )
            context['success_message'] = f'Seu Tuite de conteúdo "{content}" foi enviado'
            
    return render(request, 'post_tuite.html', context)
