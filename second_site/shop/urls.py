from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About us"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("productview/", views.prodView, name="Product View"),
    path("checkout/", views.checkOut, name="Checkout"),
]