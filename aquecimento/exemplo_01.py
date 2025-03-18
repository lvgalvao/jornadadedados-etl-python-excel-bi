from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

class AdData(BaseModel):
    organizador: str
    ano_mes: str
    dia_da_semana: str
    tipo_dia: str
    semana: str
    canal: str = Field(..., regex="^(Meta Ads|Google Ads|LinkedIn Ads)$")
    objetivo: str
    date: datetime
    campaign_name: str
    adset_name: str
    ad_name: str
    amount_spent: float = Field(..., ge=0, description="Valor gasto não pode ser negativo")
    link_clicks: Optional[int] = Field(ge=0)
    impressions: Optional[int] = Field(ge=0)
    conversions: Optional[int] = Field(ge=0)
    website_purchases: Optional[int] = Field(ge=0)
    website_purchases_conversions_value: Optional[float] = Field(ge=0)
    fase_funil: Optional[str]
    segmentacao: Optional[str]
    tipo_anuncio: str = Field(..., regex="^(Estático|Video)$")
    formato_anuncio: Optional[str]
    contexto: Optional[str]
    fase: Optional[str]

    @validator("date", pre=True)
    def parse_date(cls, value):
        """Garante que a data está no formato correto"""
        return datetime.strptime(value, "%Y-%m-%d")

    @validator("website_purchases_conversions_value")
    def check_conversion_value(cls, value, values):
        """Se houver compras, deve ter um valor de conversão"""
        if values.get("website_purchases", 0) > 0 and value is None:
            raise ValueError("O valor de conversão deve estar presente se houver compras")
        return value

# Exemplo de validação
dados = {
    "organizador": "1",
    "ano_mes": "2024 | Janeiro",
    "dia_da_semana": "Quarta-Feira",
    "tipo_dia": "Dia útil",
    "semana": "2024 | 15/01 - 21/01",
    "canal": "Meta Ads",
    "objetivo": "Leads",
    "date": "2024-01-17",
    "campaign_name": "NU | PRÉ | Foco em Leads",
    "adset_name": "LaL Compradores 2023",
    "ad_name": "Ad01 | estatico | Chamada Workshop Aberto",
    "amount_spent": 40.86,
    "link_clicks": 23,
    "impressions": 3214,
    "conversions": None,
    "website_purchases": None,
    "website_purchases_conversions_value": None,
    "fase_funil": "Estático",
    "segmentacao": None,
    "tipo_anuncio": "Estático",
    "formato_anuncio": "Postlink",
    "contexto": None,
    "fase": "Ongoing"
}

try:
    ad = AdData(**dados)
    print("Dados validados com sucesso!")
except Exception as e:
    print(f"Erro de validação: {e}")
