#!/bin/bash

# Adiciona os diretórios necessários ao PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/src

# Executa a aplicação Streamlit
streamlit run src/main.py 