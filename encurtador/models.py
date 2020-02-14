import random, string
from django.db import models

class Encurtador(models.Model):
    """ Classe utilizada para manipular urls curtas """
    # Representação da url curta
    url_curta = models.SlugField(
        max_length=30,
        unique=True,
        verbose_name='URL curta'
    )

    # A url completa de destino associada a url curta
    destino = models.URLField(
        max_length=200,
        verbose_name='URL de destino'
    )

    class Meta:
        ordering = [u'url_curta', u'destino']
        verbose_name = u'Url curta'
        verbose_name_plural = u'Urls curtas'

    def __str__(self):
        return self.url_curta

    def save(self, *args, **kwargs):
        self.url_curta = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
        super(Encurtador, self).save(*args, **kwargs)
