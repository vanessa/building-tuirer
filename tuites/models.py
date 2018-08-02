from django.db import models

from tuites.managers import TuitesManager


class Tuite(models.Model):
    content = models.CharField('Tuite', max_length=280)
    author = models.ForeignKey('users.User', verbose_name='Autor', on_delete=models.CASCADE, related_name='tuites')
    date_created = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField('users.User', blank=True)
    
    objects = TuitesManager()

    @property
    def likes_count(self):
        return self.liked_by.count()

    def get_author_username(self):
        return self.author.username

    def __str__(self):
        return f'{self.content}'

    class Meta:
        ordering = ('-date_created', )
