from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="category/", null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
