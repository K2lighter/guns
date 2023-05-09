from django.db import models


class Pistol(models.Model):
    title = models.CharField(max_length=21)
    model = models.CharField(max_length=21)
    author = models.CharField(max_length=21)
    calibre = models.CharField(max_length=21)
    country = models.CharField(max_length=21)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Пистолет'
        verbose_name_plural = 'Пистолеты'

# Pistol.objects.create(title='HK', model='USP', author='Heckler & Koch', calibre='.45 ACP', country='Germany')
