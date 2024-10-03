from django.conf import settings
import requests

def get_stock_data():
  url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey=demo'
  r = requests.get(url)
  data = r.json()
  return data