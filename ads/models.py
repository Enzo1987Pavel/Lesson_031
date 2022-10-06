from django.db import models

from users.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    name = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="ads")
    price = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=500, null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE, related_name="ads")

    def __str__(self):
        return self.name
