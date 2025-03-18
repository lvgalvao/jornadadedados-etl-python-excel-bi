import psycopg2
import pandas as pd
from src.config import DB_CONFIG

def salvar_no_postgres(df):
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criando a tabela (se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campanhas (
        id SERIAL PRIMARY KEY,
        organizador INT,
        ano_mes TEXT,
        dia_da_semana TEXT,
        tipo_dia TEXT,
        objetivo TEXT,
        date DATE,
        adset_name TEXT,
        ad_name TEXT,
        amount_spent FLOAT,
        link_clicks INT,
        impressions INT,
        conversions INT,
        fase_funil TEXT,
        segmentacao TEXT,
        tipo_anuncio TEXT,
        formato_anuncio TEXT,
        contexto TEXT,
        fase TEXT
    );
    """)

    # Inserindo dados
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO campanhas (
            organizador, ano_mes, dia_da_semana, tipo_dia, objetivo, date, adset_name, ad_name, 
            amount_spent, link_clicks, impressions, conversions, fase_funil, segmentacao, 
            tipo_anuncio, formato_anuncio, contexto, fase
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Dados salvos no PostgreSQL.")
