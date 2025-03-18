import pandas as pd

def normalizar_dados(df):
    # Convertendo valores monetários para float
    df["Amount spent"] = df["Amount spent"].replace({"R$ ": "", ",": "."}, regex=True).astype(float)

    # Convertendo datas
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Padronizando nomes de colunas (removendo espaços extras)
    df.columns = df.columns.str.strip()

    # Removendo valores nulos
    df = df.dropna()

    return df
