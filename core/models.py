from django.db import models
from datetime import datetime
from rest_api import settings


class Post(models.Model):

    options = (
        (False, 'Draft'),
        (True, 'Published'),
    )
    
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, default='')
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(choices=options, default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'
    
