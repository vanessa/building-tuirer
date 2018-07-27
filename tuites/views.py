from django.shortcuts import render
from tuites.models import Tuite

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
