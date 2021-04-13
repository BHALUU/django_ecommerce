from django.db import models
from django.utils.text import slugify

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(verbose_name='Category Name',
                            help_text='Required and unique',
                            max_length=250,
                            unique=True)

    slug = models.SlugField(
        verbose_name='Category Safe URL', max_length=250, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    is_active = models.BooleanField(default=True)

    class MPTTMETA:
        order_insertion_by = ['name', ]

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
