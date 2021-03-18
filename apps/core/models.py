from django.db import models


class BoostedModel(models.Model):
    """Abstract model with fields that all other models will have."""
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
