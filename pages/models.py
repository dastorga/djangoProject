from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from pymemcache.client import base
import memcache
from django.conf import settings


class Redirect(models.Model):

    key = models.CharField(max_length=128, null=False, blank=False, unique=True)
    url = models.CharField(max_length=254, null=False)
    active = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.key, self.url}"

    def get_redirect(self):
        """
        Obtener key
        """
        return '{} {}'.format(self.key, self.url)



@receiver(post_save, sender=Redirect)
def redirect_signal(sender, **kwargs):
    """
    Signal asociada a las actualizaciones del modelo Redirect.
    Toma todos los datos con active=True; y los coloca en una estructura de datos en cache.
    """
    redirect = kwargs['instance']

    redirects = Redirect.objects.filter(active=True)

    current_list = []
    current_list.append(redirects)

    memcached = settings.MEMCACHED_ENGINE_END_POINT
    engine_cache = False
    if memcached:
        try:
            engine_cache = memcache.Client(memcached)
        except Exception:
            print('No memcached client could be created')

    engine_cache.set('redirect_cache', current_list, settings.MEMCACHED_DEFAULT_TTL)








