from django.utils import timezone

from django.db import models


class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(default=timezone.now)
    img = models.ImageField(upload_to='static/img', default=None)

    def __str__(self):
        return f'{self.title},{self.description}'
