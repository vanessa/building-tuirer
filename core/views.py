from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from core.helpers import get_character_name, ip_info
from tuites.models import Tuite
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    context = {
        'now': datetime.now(),
        'tuites': Tuite.objects.all(),
    }
    # send_mail('Test', 'Testando', settings.DEFAULT_FROM_EMAIL, ['vanessa@vinta.com.br'])
    return render(request, 'home.html', context)
