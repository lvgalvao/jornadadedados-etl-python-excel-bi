#!/usr/bin/env python3

import os
import sys
import subprocess

# Configurar o PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")

# Adicionar diretórios ao PYTHONPATH
os.environ["PYTHONPATH"] = f"{current_dir}:{src_dir}:{os.environ.get('PYTHONPATH', '')}"

# Executar o comando streamlit
cmd = ["streamlit", "run", os.path.join(src_dir, "main.py")]

# Executar o Streamlit com o ambiente configurado
subprocess.run(cmd) 