from django.conf import settings
import requests
from decouple import config

ALPHA_KEY = config("ALPHA_KEY")

def get_stock_data(symbol, interval='1min'):
  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={ALPHA_KEY}'
  r = requests.get(url)
  data = r.json()

  time_series = data.get(f'Time Series ({interval})')

  if time_series:
    latest_time = list(time_series.keys())[0]
    latest_data = time_series[latest_time]
    close_price = latest_data['4. close']
    
    return {"symbol": symbol, 'close_price': close_price}
  
  else:
    return None