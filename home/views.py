from django.shortcuts import render
from django.http import HttpResponse
from api_integrations.alpha_vantage.stock import get_stock_data

def index(request):
  stock_info = get_stock_data('AAPL')
  context = {
    'stock_info': stock_info
  }
  return render(request, 'home/index.html', context)

