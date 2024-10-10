from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    category = Category.objects.filter(active=True)
    queryset = request.GET.get("search")
    user = User.is_staff
    if not category:
        category = None

    if queryset:
        category = Category.objects.filter(
            Q(name__icontains=queryset) | Q(product__description__icontains=queryset)
        )
        if not category:
            category = None

    return render(request, "index.html", {"categories": category, "user": user})


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
