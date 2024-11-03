from django.contrib import admin # type: ignore

# Register your models here
from .models import StockPurchase, StockSale
admin.site.register(StockPurchase) 
admin.site.register(StockSale)