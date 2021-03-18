import logging

from django.db import models
from django.core.cache import caches

from apps.core.models import BoostedModel

logger = logging.getLogger('thinkingmobile')
cache = caches['default']

class RedirectManager(models.Manager):
    def get_queryset(self):
        return super(RedirectManager, self).get_queryset().filter(active=True)


class Redirect(BoostedModel):
    key = models.CharField(max_length=254)
    url = models.URLField()
    active = models.BooleanField(default=True)

    objects = RedirectManager()
    objects_all = models.Manager()

    @classmethod
    def get_redirect(cls, key):
        """Get the information for the redirect of the cached dictionary
        :param key: str.
        :return redirect: dict."""
        redirects = cls.get_active_from_cache()
        redirect = redirects.get(key)
        if redirect:
            redirect = {'key': key, 'url': redirect}
        return redirect

    @staticmethod
    def set_active_to_cache():
        """Method to cache all active redirects.
        :return data: dict."""
        cache_key = 'all_active_redirects'
        data = dict(Redirect.objects.values_list('key', 'url'))
        cache.set(cache_key, data, 60 * 60 * 24)
        logger.info('All active redirects are cached.')
        return data

    @classmethod
    def get_active_from_cache(cls):
        """Method to obtain all active redirects from cache.
        :return data: dict."""
        cache_key = 'all_active_redirects'
        data = cache.get(cache_key)
        if not data:
            # If it is not stored, it is cached and returned
            data = cls.set_active_to_cache()
            logger.info('All active redirects are cached.')
        logger.info('Cached data is returned.')
        return data


    def __str__(self):
        return f'{self.id} - {self.url} - {self.key}'
