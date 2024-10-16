from django.shortcuts import render
from django.http import HttpResponse
from integrations.alpha_vantage.stock import get_stock_data, StockDataError

def index(request):
  stock_info = None
  error_message = None
  
  try:
    stock_info = get_stock_data('AAPL')
  except StockDataError as e:
    error_message = str(e)
    
  context = {
    'stock_info': stock_info,
    'error_message': error_message,
  }
  return render(request, 'home/index.html', context)

