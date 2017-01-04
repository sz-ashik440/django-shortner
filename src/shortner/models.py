from django.db import models
from django.conf import settings

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)



class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcode(self):
        qs = ShortURL.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.short_code = create_shortcode(q)
            q.save()
            new_codes += 1
        return 'New Codes made: {i}'.format(i=new_codes)


class ShortURLManager2(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager2, self).all(*args, **kwargs)
        qs = qs.filter(active=False)
        return qs


class ShortURL(models.Model):
    url = models.CharField(max_length=220, )
    short_code = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ShortURLManager()
    other_objects = ShortURLManager2()

    def save(self, *args, **kwargs):
        if self.short_code is None or self.short_code == '':
            self.short_code = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
