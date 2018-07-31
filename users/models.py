from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    picture = models.ImageField('Foto de perfil', default='/img/blank-pic.png')
