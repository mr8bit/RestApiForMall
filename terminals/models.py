from django.db import models


class Terminal(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название терминала")
    position = models.CharField(max_length=300, verbose_name="Позиция на карте")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Терминал"
        verbose_name_plural = "Терминалы"
