
# 💱 Yahoo Currency Pipeline

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cassiabrasileiro/yahoo-currency-pipeline/blob/main/visualizacao_moedas.ipynb)

Pipeline de ingestão, processamento paralelo e visualização de cotações cambiais via Yahoo Finance.

---

## 🚀 Objetivo

Criar um pipeline de dados que:

1. Consuma dados de câmbio para **USDBRL=X**, **EURBRL=X** e **ARSBRL=X**
2. Processe os dados em paralelo
3. Persista os dados em formato analítico (Parquet)
4. Publique uma notificação final com os registros inseridos e as falhas detalhadas
5. Forneça um notebook com análise visual dos dados

---

## 🧠 Stack Utilizada

- Python 3.9+
- pandas, requests, pyarrow
- `concurrent.futures.ThreadPoolExecutor` para paralelismo
- Jupyter Notebook para visualização
- Parquet para persistência

---

## 🛠️ Como Executar Localmente

```bash
# Clone o repositório
git clone https://github.com/cassiabrasileiro/yahoo-currency-pipeline.git
cd yahoo-currency-pipeline

# Crie e ative o ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Execute o pipeline
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
- ⚠️ **Falhas por símbolo**, com mensagens de erro detalhadas:

### Exemplos:
```bash
✅ Notificação: Registros inseridos:
→ USDBRL=X: 30 registros
→ EURBRL=X: 30 registros

⚠️ Falhas:
→ ARSBRL=X: Falha na requisição HTTP (timeout, erro 429 ou falta de acesso)
```

Isso permite entender rapidamente o que foi processado com sucesso e o que deu errado (sem logs difíceis de interpretar).

---

## 📊 Visualização dos Dados

Execute o notebook `visualizacao_moedas.ipynb` para explorar graficamente as séries históricas de câmbio.

Você também pode abrir diretamente no Colab:

[![Abrir no Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cassiabrasileiro/yahoo-currency-pipeline/blob/main/visualizacao_moedas.ipynb)

---

## 🔧 Decisões Técnicas

- Processamento paralelo com `ThreadPoolExecutor`
- Retry com backoff exponencial e headers personalizados
- Persistência em Parquet otimizado
- Estrutura de notificações robusta com separação clara entre sucesso e falha
- Código modular e pronto para escalar

---

## 🌱 Possíveis Extensões Futuras

| Ideia                          | Descrição rápida |
|-------------------------------|------------------|
| **Airflow**                   | Agendar execuções diárias e monitorar via DAG |
| **Docker**                    | Containerizar para rodar em qualquer ambiente |
| **Slack/Kafka Alerts**        | Enviar falhas críticas para canais externos |
| **Google Sheets/BigQuery**    | Persistência em destinos analíticos |
| **Testes automatizados**      | Validar schema dos dados e integração |
| **Análises mais ricas**       | Rolling averages, volatilidade, delta de variação por moeda |

---

## 👩🏽‍💻 Desenvolvido por

**Cássia Brasileiro**  
[GitHub](https://github.com/cassiabrasileiro) • [LinkedIn](https://www.linkedin.com/in/cassia-brasileiro/)
