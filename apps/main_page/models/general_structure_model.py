from django.db import models


class GeneralStructure(models.Model):    
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = "Общая структура НЦОМИД"
        verbose_name_plural = "Общие структуры НЦОМИД"
    
    def __str__(self):
        return self.title