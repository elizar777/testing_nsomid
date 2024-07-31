from django.db import models
from ckeditor.fields import RichTextField


class AboutNCOMID(models.Model):
    class Meta:
        verbose_name = 'Все об НЦОМиД'
        verbose_name_plural = 'Все об НЦОМиД'


class History(models.Model):
    description = RichTextField(verbose_name='Текст')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='history')

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'Истории'


class AboutUs(models.Model):
    description = RichTextField(verbose_name='Текст')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='about_us')

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Charter(models.Model):
    files = models.FileField(upload_to='uploads/', verbose_name='Файлы')
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='charter')

    class Meta:
        verbose_name = 'Устав'
        verbose_name_plural = 'Устав'


class Directorate(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блока')
    description = RichTextField(verbose_name='Текст')
    photo = models.ImageField(upload_to='images/', verbose_name="Фото")
    about_ncomid = models.ForeignKey(AboutNCOMID, on_delete=models.CASCADE, related_name='directorate')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дирекция'
        verbose_name_plural = 'Дирекция'









