from django.db import models

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=255, default="Unknown")
    price = models.FloatField(default=0.0)
    description = models.TextField(default="Sorry, no description yet.")
    stock = models.IntegerField(default=0)
    slug = models.CharField(max_length=255, default="")

    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



