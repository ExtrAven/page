from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "show_image",
    )
    search_fields = ("name",)
    list_filter = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "show_image",
    )
    search_fields = ("category__name",)
    list_filter = ("category__name",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
