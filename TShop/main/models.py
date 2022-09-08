from django.db import models
from django.urls import reverse


# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    price = models.FloatField(default=0.0)
    description = models.TextField(default="Sorry, no description yet.")
    stock = models.IntegerField(default=0)
    slug = models.CharField(max_length=255, default="")
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Create time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Update time")

    class Meta:
        verbose_name = "Product list"
        verbose_name_plural = "Product list"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'url_slug': self.slug})


class Categories(models.Model):
    name = models.CharField(max_length=255, default="None")
    slug = models.CharField(max_length=255, default="")

    class Meta:
        verbose_name = "Category list"
        verbose_name_plural = "Category list"
        ordering = ["name"]

    def __str__(self):
        return self.name

    # Need to create categories route
    # def get_absolute_url(self):
    #     return reverse('categories', kwargs={'url_slug': self.slug})
