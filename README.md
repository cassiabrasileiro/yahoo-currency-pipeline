
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
- Formato Parquet para eficiência
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

Os arquivos são salvos em:

```
data/YYYY-MM-DD/{symbol}.parquet
```

---

## 🔔 Notificações de Sucesso e Falha

Ao final da execução, o pipeline imprime:

- ✅ **Símbolos processados com sucesso** e quantidade de registros
- ⚠️ **Falhas detalhadas por símbolo**, incluindo causas comuns como:
  - Erros de conexão / timeout
  - API indisponível ou bloqueada (HTTP 429)
  - Arquivo vazio ou mal formatado
  - Falha no schema/tabulação

---

## 📊 Visualização Interativa

A análise gráfica dos dados pode ser visualizada diretamente no Colab:  
📎 [Notebook com visualizações no Google Colab](https://colab.research.google.com/drive/1tTJ22cdZ1PHFSHAqhMoXyFZU19_05jr7?usp=sharing)

Inclui:
- Tendência de fechamento por moeda
- Comparativo entre moedas
- Média móvel (rolling average)

---

## 🔧 Decisões Técnicas

### 1. Estratégia de Extração

> O uso de `requests` com `ThreadPoolExecutor` permite processar múltiplas chamadas simultaneamente, reduzindo o tempo total e isolando falhas por símbolo sem derrubar o pipeline todo.

### 2. Arquitetura

> O código é modular, com responsabilidades separadas por extração, transformação, persistência e notificação. Isso permite futura orquestração com ferramentas como Airflow ou inclusão de testes.

### 3. Escolha pelo Formato Parquet

> Parquet foi escolhido por ser compacto, orientado a colunas, e altamente compatível com ferramentas analíticas modernas. Comparado ao CSV, é mais eficiente tanto em leitura quanto em armazenamento.

### 4. Tratamento de Falhas

> Cada etapa do pipeline inclui tratamento específico de erro. Falhas são registradas por símbolo com mensagens como:
- `Erro 429: API bloqueada por excesso de requisições`
- `Dados retornaram vazios`
- `Erro de leitura no Parquet`
- `Problema de schema ou timestamp inválido`

---

## 🌱 Próximas Expansões

| Ideia                          | Descrição rápida |
|-------------------------------|------------------|
| **Airflow**                   | Orquestrar execução diária |
| **Docker**                    | Containerização para deploy |
| **Slack/Kafka Alerts**        | Notificações automáticas |
| **Persistência no BigQuery**  | Destino analítico para dashboard |
| **Testes e observabilidade**  | Alertas e validação de schema |

---

## 👩🏽‍💻 Desenvolvido por

**Cássia Brasileiro**  
[GitHub](https://github.com/cassiabrasileiro) • [LinkedIn](https://www.linkedin.com/in/cassiasantos96/)
