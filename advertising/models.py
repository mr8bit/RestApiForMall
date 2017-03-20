from django.db import models


# Create your models here.
class PlayListAdvertising(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    ads = models.ManyToManyField('Advertising', verbose_name="Рекламный список")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Список рекламы"
        verbose_name_plural = "Список рекламы"


class Advertising(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    file = models.FileField(upload_to='ads/', verbose_name="Файл")
    duration = models.IntegerField(default=0, verbose_name="Время показа", help_text="в секундах")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Реклама"
        verbose_name_plural = "Реклама"
