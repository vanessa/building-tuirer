from django.shortcuts import render
from django.http import HttpResponse

# ✔️ Checkpoint:
# Criar uma função da API que você selecionou
# na primeira aula para retornar como a resposta.

def index(request):
    return HttpResponse('Olá')
