import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import ace_tools as tools  # Ferramenta para exibir os gráficos

def gerar_insights(df):
    # Criando diretório para salvar gráficos
    os.makedirs("data/insights", exist_ok=True)

    # 🔹 Ajustando tipos de dados
    df["Amount spent"] = df["Amount spent"].astype(float)
    df["Link clicks"] = df["Link clicks"].astype(int)
    df["Conversions"] = df["Conversions"].astype(int)

    # 🔹 Gráfico 1: Gasto por Campanha
    plt.figure(figsize=(12, 6))
    sns.barplot(x=df["AdSet name"], y=df["Amount spent"], ci=None, palette="viridis")
    plt.xticks(rotation=90)
    plt.xlabel("Campanhas")
    plt.ylabel("Gasto Total (R$)")
    plt.title("💰 Gasto por Campanha")
    plt.tight_layout()
    plt.savefig("data/insights/gasto_por_campanha.png")
    plt.close()

    # 🔹 Gráfico 2: Cliques por Anúncio
    plt.figure(figsize=(12, 6))
    sns.barplot(x=df["Ad name"], y=df["Link clicks"], ci=None, palette="coolwarm")
    plt.xticks(rotation=90)
    plt.xlabel("Anúncio")
    plt.ylabel("Total de Cliques")
    plt.title("🖱️ Cliques por Anúncio")
    plt.tight_layout()
    plt.savefig("data/insights/cliques_por_anuncio.png")
    plt.close()

    # 🔹 Gráfico 3: Conversões por Fase do Funil
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df["Fase Funil"], y=df["Conversions"], palette="magma")
    plt.xlabel("Fase do Funil")
    plt.ylabel("Total de Conversões")
    plt.title("🔄 Conversões por Fase do Funil")
    plt.tight_layout()
    plt.savefig("data/insights/conversoes_por_fase.png")
    plt.close()

    print("✅ Insights gerados com sucesso! Verifique a pasta 'data/insights'.")

    # Exibir gráficos no ChatGPT
    tools.display_dataframe_to_user(name="Resumo das Campanhas", dataframe=df[["AdSet name", "Amount spent", "Link clicks", "Conversions"]])
