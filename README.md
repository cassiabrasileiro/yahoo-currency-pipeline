
# 💱 Yahoo Currency Pipeline

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tTJ22cdZ1PHFSHAqhMoXyFZU19_05jr7?usp=sharing)

Pipeline de ingestão, processamento paralelo e visualização de cotações cambiais via Yahoo Finance, com foco em confiabilidade, desempenho e facilidade de análise.

---

## 🚀 Objetivo

Criar um pipeline de dados que:

1. Consuma dados de câmbio para **USDBRL=X**, **EURBRL=X** e **ARSBRL=X**
2. Processe os dados em paralelo
3. Persista os dados em formato analítico (Parquet)
4. Publique notificações com os registros processados e falhas diagnosticadas
5. Disponibilize uma visualização interativa via Google Colab

---

## 🧠 Stack Utilizada

- Python 3.9+
- pandas, requests, pyarrow
- `ThreadPoolExecutor` para paralelismo
- Parquet para persistência eficiente
- Google Colab para visualização

---

## 🛠️ Como Executar Localmente

```bash
git clone https://github.com/cassiabrasileiro/yahoo-currency-pipeline.git
cd yahoo-currency-pipeline

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python main.py
```

---

## 📂 Estrutura de Saída

Os arquivos são salvos localmente em:

```
data/YYYY-MM-DD/{symbol}.parquet
```

> ⚠️ A estrutura atual salva em disco local, mas pode ser facilmente adaptada para salvar em buckets (como S3 ou GCS) utilizando bibliotecas como `smart_open`, `s3fs` ou `gcsfs`.

---

## 🔧 Decisões Técnicas

### 1. Estratégia de Extração

- Utilizamos chamadas simultâneas via `ThreadPoolExecutor` para paralelizar a coleta dos dados de múltiplos símbolos.
- A extração inclui verificação de integridade temporal, validando se os dados possuem entradas do **dia atual**. Caso contrário, é registrada uma falha (ex: "dados desatualizados").

### 2. Processamento e Modelagem

- A estrutura tabular contém colunas como: `symbol`, `timestamp`, `open`, `close`, `high`, `low`, `volume`.
- Com esses campos é possível:
  - Traçar tendências temporais (timestamp)
  - Calcular volatilidade (high - low)
  - Medir liquidez e comportamento de abertura/fechamento (open, close, volume)
- O schema foi pensado para atender análises descritivas, séries temporais e visualizações exploratórias.

### 3. Persistência

- O formato **Parquet** foi escolhido por ser leve, comprimido e orientado a colunas — ideal para consumo por ferramentas como Spark, BigQuery, Pandas.
- A estrutura de pastas por data permite versionamento temporal, rastreabilidade e uso em camadas como *landing* ou *bronze*.

### 4. Notificação

- O pipeline envia notificações com os resultados da execução.
- Suporte a:
  - Prints locais (simulação)
  - Slack Webhook (opcional)
  - Email (via SMTP - recomendado para alertas reais)

---

## 🔔 Exemplo de Notificação por Email

```text
✅ Registros inseridos com sucesso:
  - USDBRL=X: 30 registros
  - EURBRL=X: 30 registros

⚠️ Falhas detectadas:
  - ARSBRL=X: Dados desatualizados ou API bloqueada (429)
```

---

## 📊 Visualização Interativa

📎 [Notebook com visualizações no Google Colab](https://colab.research.google.com/drive/1tTJ22cdZ1PHFSHAqhMoXyFZU19_05jr7?usp=sharing)

Inclui:
- Tendência de fechamento por moeda
- Comparativo entre moedas
- Média móvel (rolling average)

---

## 🌱 Próximas Expansões

| Ideia                          | Descrição rápida |
|-------------------------------|------------------|
| **Airflow**                   | Orquestrar execução diária |
| **Docker**                    | Containerização para deploy |
| **Slack/Email/Kafka Alerts**  | Notificações automáticas |
| **Persistência no BigQuery**  | Destino analítico para dashboard |
| **Testes e observabilidade**  | Alertas e validação de schema |

---

## 👩🏽‍💻 Desenvolvido por

**Cássia Brasileiro**  
[GitHub](https://github.com/cassiabrasileiro) • [LinkedIn](https://www.linkedin.com/in/cassiasantos96/)
