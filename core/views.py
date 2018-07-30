from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from core.helpers import get_character_name, ip_info
from tuites.models import Tuite


def index(request):
    context = {
        'now': datetime.now(),
        'tuites': Tuite.objects.all(),
    }
    return render(request, 'home.html', context)
