from django.db import models


class TuitesManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(content__icontains=query) |
            models.Q(author__username__icontains=query)
        )
