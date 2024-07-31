from django.db import models
from ckeditor.fields import RichTextField


class ScientificActivity(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Текст блока Научной деятельности')

    class Meta:
        verbose_name = "Начная деятельность"
        verbose_name_plural = "Научные деятельности"

    def __str__(self):
        return self.title


class ScientificActivityContent(models.Model):
    title_content = models.TextField(verbose_name='Заголовок контента')
    text_content = RichTextField(verbose_name='Текст контента')
    block = models.ForeignKey(ScientificActivity,
                              on_delete=models.CASCADE,
                              verbose_name='Блок',
                              related_name='content')

    class Meta:
        verbose_name = "Контент"
        verbose_name_plural = "Контенты"

    def __str__(self):
        return self.title_content

