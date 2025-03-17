from pydantic import BaseModel, validator
from typing import Optional

class UserModel(BaseModel):
    Nome: str
    Idade: int
    Email: str
    
    @validator('Nome')
    def nome_valido(cls, v):
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        return v
    
    @validator('Idade')
    def idade_valida(cls, v):
        if v < 0 or v > 120:
            raise ValueError('Idade deve estar entre 0 e 120 anos')
        return v
    
    @validator('Email')
    def email_valido(cls, v):
        if '@' not in v:
            raise ValueError('Email inválido, deve conter @')
        return v