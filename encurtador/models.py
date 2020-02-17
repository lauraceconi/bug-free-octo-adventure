import random, string
from django.db import models

class URLCurta(models.Model):
    """ 
    Classe utilizada para manipular urls curtas 
    """    
    # Representação da URL curta
    slug = models.SlugField(
        max_length=30,
        unique=True
    )

    # A url completa de destino associada a URL curta
    destino = models.URLField(max_length=200)

    # Quantidade de acessos à url
    acessos = models.PositiveIntegerField(default=0)

    # Data e hora de criação da URL, para ordenação
    data_criacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Representação do objeto
        """
        return self.slug

    def save(self, *args, **kwargs):
        """
        Método sobreescrito para criar e atribuir a URL curta
        """
        if self.pk is None:
            self.slug = ''.join([random.choice(string.ascii_letters) for _ in range(6)])
        super(URLCurta, self).save(*args, **kwargs)
