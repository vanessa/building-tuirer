from django.db import models
from tuites.managers import TuitesManager


class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280, default='Olá!')
    author = models.ForeignKey('users.User', verbose_name='Autor', default=1, on_delete=models.SET_DEFAULT, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)
    
    objects = TuitesManager()

    def get_author_username(self):
        return self.author.username

    def __str__(self):
        return f'{self.author.username}: {self.content}'

    class Meta:
        ordering = ('content', )