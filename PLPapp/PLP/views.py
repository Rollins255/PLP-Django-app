from django.shortcuts import render # type: ignore

# Create your views here.
from .models import StockPurchase, StockSale
from django.db.models import Sum # type: ignore
def stock_report(request):
    purchases = StockPurchase.objects.all() 
    sales = StockSale.objects.all() 
    total_purchases = purchases.aggregate(Sum('quantity')) 
    total_sales = sales.aggregate(Sum('quantity'))

    context = {
        'purchases': purchases, 'sales': sales, 
        'total_purchases': total_purchases['quantity__sum'], 
        'total_sales': total_sales['quantity__sum'],
    }
    return render(request, 'PLP/stock_report.html',)