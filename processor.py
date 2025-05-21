
import pandas as pd

def process_data(symbol, json_data):
    try:
        result = json_data['chart']['result'][0]
        timestamps = result['timestamp']
        quotes = result['indicators']['quote'][0]

        df = pd.DataFrame(quotes)
        df['timestamp'] = pd.to_datetime(timestamps, unit='s')
        df['symbol'] = symbol
        return df[['symbol', 'timestamp', 'open', 'high', 'low', 'close', 'volume']]
    except Exception as e:
        print(f"Erro ao processar {symbol}: {e}")
        return None
