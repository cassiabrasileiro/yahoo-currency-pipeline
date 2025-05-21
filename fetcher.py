
import requests
from utils import retry_request

def fetch_currency_data(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval=1d&range=30d"
    response = retry_request(url)
    if response is None:
        return None

    if response.status_code != 200:
        print(f"[Erro {symbol}] Código HTTP {response.status_code}")
        return None

    return response.json()
