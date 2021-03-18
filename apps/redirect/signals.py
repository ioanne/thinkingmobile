import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.redirect.models import Redirect

logger = logging.getLogger('thinkingmobile')


@receiver(post_save, sender=Redirect)
def cache_data_on_save(sender, instance, created, **kwargs):
    Redirect.set_active_to_cache()
    logger.info('Cached data from a signal')
