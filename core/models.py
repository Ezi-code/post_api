from django.db import models
from datetime import datetime
from accounts.models import User



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
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}'
    
