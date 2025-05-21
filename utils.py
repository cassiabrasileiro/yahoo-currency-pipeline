
import time
import requests

def retry_request(url, retries=5, backoff=2):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            print(f"Erro {response.status_code}. Tentando novamente...")
        except Exception as e:
            print(f"Erro na requisição: {e}")
        time.sleep(backoff * (attempt + 1))
    return None
