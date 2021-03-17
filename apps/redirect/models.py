from django.db import models
from django.core.cache import caches

from apps.core.models import BoostedModel


class Redirect(BoostedModel):
    key = models.CharField(max_length=254)
    url = models.URLField()
    active = models.BooleanField(default=True)

    @property
    def cache(self):
        return caches['default']
