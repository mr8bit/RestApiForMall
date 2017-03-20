from django.db import models
import datetime
from unidecode import unidecode
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300, default='', verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


def make_upload_path(instance, filename):
    """
    Создание загрузочной папки для магазинов
    :param instance:
    :param filename:
    :return:
    """
    folder = slugify(unidecode(instance.name))
    print(folder)
    return u'shops/%s/%s' % (folder, filename)


class Shop(models.Model):
    name = models.CharField(max_length=400, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")
    logo = models.ImageField(upload_to=make_upload_path, verbose_name="Логотип")
    photo = models.ImageField(upload_to=make_upload_path, verbose_name="Фото")
    category = models.ForeignKey('Category', default='', verbose_name="Категория")
    mapID = models.CharField(max_length=300, default='Позиция на карте')
    mapLogo = models.ImageField(upload_to=make_upload_path, verbose_name="Логотип на карте")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Sale(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')
    image = models.ImageField(upload_to="sales/", verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
