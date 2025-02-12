from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About us"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Tracking Status"),
    path("search/", views.search, name="Search"),
    path("products/<int:p_id>", views.prodView, name="Product View"),
    path("checkout/", views.checkOut, name="Checkout"),
    path("handleRequest/", views.handleRequest, name="Handle Payment Request"),
]