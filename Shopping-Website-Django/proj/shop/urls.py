from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("",views.index,name='index'),
    path("about/",views.about,name='aboutus'),
    path("contact/",views.contact,name='contactus'),
    path("contact_page/",views.contact_page,name='contact_page'),
    path("search",views.search,name='search'),
    path("productview/",views.productview,name='productview'),
    path('order/<product_id>',views.order,name='order'),
    path('cart/',views.cart,name='cart'),
    path('delete/<product_id>',views.delete,name='delete')
]
