from django.db import models

from shop.models import Item


class Cart(models.Model):
    user_id = models.CharField(max_length=255)
    products = models.ManyToManyField(Item)

    def __str__(self) -> str:
        return f'{self.user_id}: {self.products.values_list("name", flat=True)}'
