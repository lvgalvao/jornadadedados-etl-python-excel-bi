import pandas as pd

# 📌 Definir colunas esperadas
colunas_esperadas = [
    "Organizador", "Ano/Mes", "Dia_da_Semana", "Tipo_Dia", "Objetivo",
    "Date", "AdSet_name", "Ad_name", "Amount_spent", "Link_clicks",
    "Impressions", "Conversions", "Fase_Funil", "Segmentação",
    "Tipo_de_Anúncio", "Contexto", "Fase"
]

# 📌 Carregar o DataFrame
df = pd.read_csv("data/jornada_de_dados_2024.csv")

# 📌 Renomear colunas removendo espaços extras e padronizando
df.columns = df.columns.str.strip().str.replace(" ", "_")

# 📌 Identificar colunas faltando
colunas_faltando = set(colunas_esperadas) - set(df.columns)

# 📌 Identificar colunas extras (que não deveriam estar no DataFrame)
colunas_extras = set(df.columns) - set(colunas_esperadas)

# 📌 Exibir os resultados
if colunas_faltando:
    print(f"🚨 Colunas faltando: {colunas_faltando}")
else:
    print("✅ Todas as colunas obrigatórias estão presentes!")

if colunas_extras:
    print(f"⚠️ Colunas extras encontradas: {colunas_extras}")
else:
    print("✅ Nenhuma coluna extra encontrada!")
