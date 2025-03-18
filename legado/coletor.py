import streamlit as st

# Configuração da página Streamlit
st.set_page_config(
    page_title="Sistema de ETL",
    page_icon="📊",
    layout="wide"
)

# Título e descrição da aplicação
st.title("📊 Sistema de ETL - Excel para Banco de Dados")

st.markdown("""
    Este aplicativo será desenvolvido para carregar arquivos Excel ou CSV, validar os dados e salvá-los no banco de dados.

    O que iremos construir:
    1. Upload de arquivos Excel/CSV
    2. Pré-visualização dos dados
    3. Validação automática dos dados
    4. Salvamento dos dados no banco de dados

    No momento, este sistema ainda está em desenvolvimento.
""")

# Seção de upload de arquivos
st.header("Upload de Arquivo")
uploaded_file = st.file_uploader("Escolha um arquivo Excel ou CSV", type=["xlsx", "csv"])

if uploaded_file is not None:
    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso!")
    st.warning("🚧 As funcionalidades de pré-visualização e processamento ainda estão em desenvolvimento!")

# Botões de funcionalidades futuras
if st.button("Validar Dados"):
    st.warning("🚧 Funcionalidade em desenvolvimento!")

if st.button("Salvar no Banco de Dados"):
    st.warning("🚧 Funcionalidade em desenvolvimento!")

if st.button("Ver Dados no Banco"):
    st.warning("🚧 Funcionalidade em desenvolvimento!")

# Rodapé da aplicação
st.markdown("---")
st.markdown("### Desenvolvido para o projeto de ETL com Python, Excel e BI")
