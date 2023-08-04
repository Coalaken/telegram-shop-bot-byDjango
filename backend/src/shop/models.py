from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    
class Item(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=255)
    slug = models.SlugField(max_length=255) 
    img = models.TextField(null=True) 
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 related_name='items',
                                 verbose_name='Категория')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, 
                                   verbose_name='Последнее обновление')

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-created']
        # indexes = [
        #     models.Index(fields=['category'])
        # ]
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.price}'

