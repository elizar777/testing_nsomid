from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    text = models.CharField(max_length=100, verbose_name='текст')
    images = models.ImageField(upload_to='banner/', verbose_name='фото')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннер'

    def __str__(self):
        return self.title
