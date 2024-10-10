from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True, upload_to="category")
    active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def show_image(self):
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width="100" height="100" />'
            )
        else:
            return "No Hay Imagen"

    show_image.short_description = "Imagen"


class Product(models.Model):
    description = models.TextField(help_text="Descripción del producto")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    width = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    radius = models.DecimalField(max_digits=10, decimal_places=0, default=0)

    def __str__(self):
        return f"Pertenece a {self.category.name}"

    def show_image(self):
        return format_html(
            f'<img src="{self.category.image.url}" width="200" height="200" />'
        )

    show_image.short_description = "Imagen"
