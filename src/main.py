import pandas as pd
import streamlit as st
import sqlite3
import os
import sys

# Adicionar o diretório pai ao path (alternativa a usar src. nos imports)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importações locais
from src.validators import validar_planilha
from src.database import conectar_db, salvar_dados
from src.models import UserModel

# Configuração da página Streamlit
st.set_page_config(
    page_title="Sistema de ETL",
    page_icon="📊",
    layout="wide"
)

# Título e descrição da aplicação
st.title("📊 Sistema de ETL - Excel para Banco de Dados")
st.markdown("""
    Este aplicativo permite carregar arquivos Excel ou CSV, validar os dados e salvá-los no banco de dados.
    
    ### Como usar:
    1. Faça upload do seu arquivo Excel/CSV
    2. Verifique a pré-visualização dos dados
    3. Clique em 'Validar Dados' para checar se há erros
    4. Se não houver erros, clique em 'Salvar no Banco de Dados'
""")

# Inicialização do banco de dados se não existir
def inicializar_db():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Idade INTEGER,
        Email TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Inicializa o banco de dados
inicializar_db()

# Upload de arquivo
st.header("Upload de Arquivo")
uploaded_file = st.file_uploader("Escolha um arquivo Excel ou CSV", type=["xlsx", "csv"])

if uploaded_file is not None:
    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")
    
    # Ler o arquivo com pandas dependendo do tipo
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Mostrar tabela de dados
    st.header("Pré-visualização dos Dados")
    st.dataframe(df)
    
    # Botão para validar dados
    if st.button("Validar Dados"):
        st.header("Resultados da Validação")
        erros = validar_planilha(df)
        
        if erros:
            st.error("Encontramos erros nos dados:")
            for erro in erros:
                st.warning(erro)
        else:
            st.success("Dados validados com sucesso! Não foram encontrados erros.")
            
            # Botão para salvar no banco de dados
            if st.button("Salvar no Banco de Dados"):
                try:
                    # Salvar cada linha no banco de dados
                    contador = 0
                    for _, row in df.iterrows():
                        valores = (row['Nome'], row['Idade'], row['Email'])
                        salvar_dados(valores)
                        contador += 1
                    
                    st.success(f"✅ {contador} registros salvos com sucesso no banco de dados!")
                    
                    # Opção para ver os dados salvos
                    if st.button("Ver Dados no Banco"):
                        conn = conectar_db()
                        dados_salvos = pd.read_sql_query("SELECT * FROM users", conn)
                        conn.close()
                        
                        st.header("Dados no Banco")
                        st.dataframe(dados_salvos)
                
                except Exception as e:
                    st.error(f"Erro ao salvar dados: {str(e)}")
    
    # Informações sobre o arquivo
    st.sidebar.header("Informações do Arquivo")
    st.sidebar.info(f"""
    **Nome do arquivo:** {uploaded_file.name}
    **Tamanho:** {uploaded_file.size} bytes
    **Colunas:** {', '.join(df.columns)}
    **Registros:** {len(df)}
    """)

# Rodapé da aplicação
st.markdown("---")
st.markdown("### Desenvolvido para o projeto de ETL com Python, Excel e BI")