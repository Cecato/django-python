from django.conf import settings
import requests
from decouple import config

ALPHA_KEY = config("ALPHA_KEY")

class StockDataError(Exception):
  # This class is intentionally left empty to create a custom exception type
  pass

def get_stock_data(symbol, interval='1min'):
  url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={ALPHA_KEY}'
  
  try:
    r = requests.get(url)
    r.raise_for_status()
    
  except requests.exceptions.HTTPError as http_err:
    raise StockDataError(f"HTTP error when accessing stock data for {symbol}: {http_err}")
  
  except requests.exceptions.RequestException as req_err:
    raise StockDataError(f"Error when accessing the API for stock {symbol}: {req_err}")

  data = r.json()

  time_series = data.get(f'Time Series ({interval})')

  if time_series:
    latest_time = list(time_series.keys())[0]
    latest_data = time_series[latest_time]
    close_price = latest_data['4. close']
    
    return {"symbol": symbol, 'close_price': close_price}
  
  elif "Error Message" in data:
    raise StockDataError(f"API error {data['Error Message']}")
  
  elif "Note" in data:
    raise StockDataError(f"Stock data for {symbol} not found or invalid response.")
  
  else:
    return None