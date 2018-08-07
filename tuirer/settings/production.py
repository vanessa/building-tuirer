from .base import *
import django_heroku

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

django_heroku.settings(locals())