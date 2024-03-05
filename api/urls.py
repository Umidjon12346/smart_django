from django.urls import path
from .views import add_product,delete, get_product,get_products,get_by_name,get_color,get_date,get_price,get_endWith,get_brend,do_updates
urlpatterns = [
    path("add/",add_product),
    path("delete/<int:pk>",delete),
    path("get/<int:pk>",get_product),
    path("getall/",get_products),
    path("get/<str:pk>",get_by_name),
    path("getcolor/<str:kk>",get_color),
    path("getpr/<int:pk>/<int:pp>",get_price),
    path("getdate/<int:pk>",get_date),
    path("getend/<str:pk>",get_endWith),
    path("getbrend/",get_brend),
    path("update/<int:pk>",do_updates)
]