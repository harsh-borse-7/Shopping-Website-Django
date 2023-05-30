from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Order
from .models import Feedback

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Feedback)