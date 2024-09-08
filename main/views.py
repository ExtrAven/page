from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    category = Category.objects.all()
    return render(request, "index.html", {"categories": category})


def category_detail(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category_id=id)
    return render(
        request, "category_detail.html", {"category": category, "products": products}
    )


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")
