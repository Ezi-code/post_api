"""choices file."""

from django.db.models import TextChoices

class PostStatus(TextChoices):
    """Post status choices."""

    DRAFT = "Draft", "Draft"
    PUBLISHED = "Published", "Published"