from django.db import models
from django.utils.html import format_html


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(
        choices=[
            ("Hogar", "Hogar"),
            ("Muebles", "Muebles"),
        ],
        max_length=50,
        default="General",
    )
    image = models.ImageField(null=True, blank=True, upload_to="category")

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
    image_1 = models.ImageField(null=True, blank=True, upload_to="product_1")
    image_2 = models.ImageField(null=True, blank=True, upload_to="product_2")
    image_3 = models.ImageField(null=True, blank=True, upload_to="product_3")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pertenece a la categoría {self.category.name}"

    def show_image(self):
        return format_html(f'<img src="{self.image_1.url}" width="200" height="200" />')

    show_image.short_description = "Imagen"
