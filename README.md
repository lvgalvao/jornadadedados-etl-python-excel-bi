# Sistema de ETL - Python, Excel e BI

Este projeto implementa um sistema de ETL (Extract, Transform, Load) para processar dados de arquivos Excel ou CSV, validá-los e salvá-los em um banco de dados SQLite.

## Funcionalidades

- Upload de arquivos Excel (.xlsx) ou CSV (.csv)
- Validação de dados com regras de negócio definidas
- Visualização dos dados em formato tabular
- Armazenamento em banco de dados SQLite
- Interface amigável construída com Streamlit

## Requisitos

- Python 3.8+
- Bibliotecas listadas em `requirements.txt`

## Como executar

1. Clone este repositório
2. Instale as dependências:
```
pip install -r requirements.txt
```
3. Execute a aplicação (escolha uma das opções):

**Opção 1 (Recomendada):**
```
python app.py
```

**Opção 2:**
```
streamlit run src/main.py
```

## Estrutura do projeto

- `/src`: Código-fonte da aplicação
  - `main.py`: Aplicação Streamlit
  - `models.py`: Modelos de dados com validações
  - `validators.py`: Funções de validação
  - `database.py`: Funções para manipulação do banco de dados
- `/data`: Pasta para arquivos de dados de exemplo

## Como usar

1. Inicie a aplicação conforme as instruções acima
2. Faça upload de um arquivo Excel ou CSV com as colunas: Nome, Idade e Email
3. Visualize os dados na interface
4. Valide os dados clicando no botão correspondente
5. Se não houver erros, salve os dados no banco de dados

## Regras de validação

- Nome: Mínimo de 3 caracteres
- Idade: Entre 0 e 120 anos
- Email: Deve conter o caractere '@'