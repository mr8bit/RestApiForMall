from django.db import models


class UserPhoto(models.Model):
    email = models.CharField(max_length=300, verbose_name="Почта пользователя")
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name="Фото")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Фото пользователя"
        verbose_name_plural = "Фото пользователей"