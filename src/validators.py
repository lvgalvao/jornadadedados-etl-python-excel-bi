import pandas as pd
from typing import List
from .models import UserModel

def validar_planilha(df: pd.DataFrame) -> List[str]:
    erros = []
    
    for index, row in df.iterrows():
        try:
            UserModel(**row)  # Valida usuário com Pydantic
        except Exception as e:
            erros.append(f'Erro na linha {index + 1}: {str(e)}')

    return erros