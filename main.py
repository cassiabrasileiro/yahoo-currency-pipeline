
from fetcher import fetch_currency_data
from processor import process_data
from writer import save_to_parquet
from notifier import notify
from concurrent.futures import ThreadPoolExecutor

CURRENCY_SYMBOLS = ["USDBRL=X", "EURBRL=X", "ARSBRL=X"]

def run_pipeline():
    successes = {}
    failures = {}

    with ThreadPoolExecutor(max_workers=3) as executor:
        raw_data = list(executor.map(fetch_currency_data, CURRENCY_SYMBOLS))

    for symbol, data in zip(CURRENCY_SYMBOLS, raw_data):
        if data is None:
            failures[symbol] = "Falha na requisição HTTP (timeout, erro 429 ou falta de acesso)"
            continue

        try:
            df = process_data(symbol, data)
            if df is None or df.empty:
                failures[symbol] = "Dados processados estão vazios ou mal formatados"
                continue
            save_to_parquet(df)
            successes[symbol] = len(df)
        except Exception as e:
            failures[symbol] = f"Erro inesperado: {str(e)}"

    notify(successes, failures)

if __name__ == "__main__":
    run_pipeline()
