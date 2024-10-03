from django.shortcuts import render
from django.http import HttpResponse
from api_integrations.alpha_vantage.stock import get_stock_data

def index(request):
  return render(request, 'home/index.html', {'mensagem': get_stock_data})

