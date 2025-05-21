
# 💱 Pipeline de Moedas - Yahoo Finance

## 📌 Objetivo
Ingestão de dados de câmbio via Yahoo Finance, com processamento paralelo, persistência em Parquet e tratamento de falhas.

## 🚀 Como executar

```bash
pip install -r requirements.txt
python main.py
```

## 📂 Estrutura de saída
Os arquivos são salvos em `data/YYYY-MM-DD/` no formato `.parquet`.

## 🔔 Notificação
Ao final, o pipeline imprime os registros inseridos por símbolo e qualquer erro ocorrido durante a execução.

## 🔧 Decisões técnicas
- Processamento paralelo com `ThreadPoolExecutor`
- Retry com backoff exponencial
- Cabeçalho User-Agent para evitar bloqueios
- Persistência em Parquet com schema tabular
- Notificações de falhas com mensagens específicas por símbolo
