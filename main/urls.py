from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("<int:id>/", category_detail, name="category_detail"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
]
