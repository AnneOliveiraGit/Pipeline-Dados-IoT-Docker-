# 📡 Pipeline de Dados com IoT e Docker

Este projeto demonstra a construção de um pipeline completo para processar dados de temperatura de dispositivos IoT e armazená-los em um banco PostgreSQL em contêiner Docker. Um dashboard interativo com Streamlit exibe visualizações e insights dos dados.

---

## 📁 Estrutura do Projeto

```
├── connect.py              # Teste de conexão com PostgreSQL
├── inserir_dados.py        # Inserção de dados do CSV no banco
├── views.sql               # Criação das views SQL
├── dashboard.py            # Dashboard interativo com Streamlit
├── IOT-temp.csv            # Conjunto de dados original
```

---

## ⚙️ Tecnologias Utilizadas

- Python 3.10+
- Docker + PostgreSQL
- SQLAlchemy + Pandas
- Streamlit + Plotly
- Dataset: [Temperature Readings - Kaggle](https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices)

---

## 🚀 Como Executar

### 1. Suba o container PostgreSQL:

```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=SuaSenha -p 5432:5432 -d postgres
```

### 2. Instale as dependências:

```bash
pip install pandas sqlalchemy psycopg2-binary streamlit plotly
```

### 3. Insira os dados no banco:

```bash
python inserir_dados.py
```

### 4. Crie as views SQL (use pgAdmin ou DBeaver com o conteúdo de `views.sql`)

### 5. Execute o dashboard:

```bash
streamlit run dashboard.py
```

---

## 📊 Dashboard Interativo

O dashboard exibe:

- 📌 **Média de temperatura por dispositivo**  
- ⏱️ **Número de leituras por hora**  
- 🌡️ **Temperaturas máximas e mínimas por dia**

---

## 🧠 Insights dos Dados

- Dispositivos com temperaturas médias elevadas foram facilmente identificados.
- Picos de leituras ocorrem majoritariamente durante horários específicos do dia.
- Oscilações extremas de temperatura em determinados dias podem indicar problemas no ambiente ou sensores.

---

## 📝 Observações

- Views foram ajustadas com cast explícito em `noted_date` por ser texto.
- O campo `"room_id/id"` foi mantido com aspas por conter caractere especial.
- É recomendado normalizar nomes de colunas futuramente.

---
