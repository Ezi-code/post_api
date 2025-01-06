from django.db import models
from datetime import datetime
from rest_api import settings
from .choices import PostStatus


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    """Post model."""

    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100, null=True)
    content = models.TextField()
    status = models.BooleanField(choices=PostStatus.choices, default=PostStatus.DRAFT)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="post_author",
    )

    def __str__(self):
        return f"{self.title}"
