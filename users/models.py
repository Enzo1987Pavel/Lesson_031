from django.db import models


class Location(models.Model):
    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=15, decimal_places=10)
    lng = models.DecimalField(max_digits=15, decimal_places=10)

    def __str__(self):
        return self.name


class UserRoles:
    USER = "member"
    ADMIN = "admin"
    MODERATOR = "moderator"
    choices = (
        ("Пользователь", USER),
        ("Администратор", ADMIN),
        ("Модератор", MODERATOR)
    )


class User(models.Model):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(choices=UserRoles.choices, default="member", max_length=16)
    age = models.PositiveIntegerField(null=True)
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username
