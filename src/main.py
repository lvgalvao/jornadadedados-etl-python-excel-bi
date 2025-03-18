import pandas as pd
from src.validate import validar_dados
from src.normalize import normalizar_dados
from src.database import salvar_no_postgres
from src.insights import gerar_insights

def main():
    file_path = "data/input.xlsx"
    
    # 1️⃣ Carregar planilha
    df = pd.read_excel(file_path)

    # 2️⃣ Validar dados
    erros = validar_dados(df)
    if erros:
        print("⚠ Erros encontrados:", erros)
        return
    
    # 3️⃣ Normalizar dados
    df_corrigido = normalizar_dados(df)

    # 4️⃣ Salvar no banco de dados
    salvar_no_postgres(df_corrigido)

    # 5️⃣ Gerar insights
    gerar_insights(df_corrigido)

    print("✅ Processo concluído com sucesso!")

if __name__ == "__main__":
    main()
