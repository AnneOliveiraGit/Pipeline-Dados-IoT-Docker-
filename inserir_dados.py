import pandas as pd
from sqlalchemy import create_engine

# Caminho para o CSV baixado do Kaggle
csv_file = r"C:\Caminho\Para\Csv\Do\kaggle"  # Substitua pelo nome exato se for diferente

# Configuração da conexão com o PostgreSQL
engine = create_engine('postgresql://postgres:SuaSenha@localhost:5432/postgres')

# Leitura do CSV
df = pd.read_csv(csv_file)

# Inserção dos dados na tabela
try:
    df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
    print("Dados inseridos com sucesso na tabela 'temperature_readings'.")
except Exception as e:
    print("Erro ao inserir os dados:", e)
