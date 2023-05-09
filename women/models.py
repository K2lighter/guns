from django.db import models


class Women(models.Model):
    title = models.CharField('Название', max_length=50)
    content = models.TextField('Контент', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Женщина'
        verbose_name_plural = 'Женщины'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

    def __str__(self):
        return self.name

