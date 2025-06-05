from sqlalchemy import create_engine, text
import pandas as pd

# String de conexão com caracteres especiais escapados
engine = create_engine('postgresql://postgres:SuaSenha@localhost:5432/postgres')

# Tenta executar um SELECT simples
try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        for row in result:
            print("Conectado com sucesso! Versão do PostgreSQL:", row[0])
except Exception as e:
    print("Erro ao conectar:", e)
