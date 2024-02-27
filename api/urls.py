from django.urls import path
from .views import add_product,delete, get_product
urlpatterns = [
    path("add/",add_product),
    path("delete/<int:pk>",delete),
    path("get/<int:pk>",get_product)
]