import json
import pandas as pd
import pandera as pa
from pandera.typing import Series

# Definição do Schema com Pandera
class LeadFunnelSchema(pa.DataFrameModel):

    Organizador: Series[int] = pa.Field(ge=1)
    Ano_Mes: Series[str] = pa.Field(str_startswith="2024")
    Dia_da_Semana: Series[str] = pa.Field(isin=["Segunda-Feira", "Terça-Feira", "Quarta-Feira",
                                                 "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"])
    Tipo_Dia: Series[str] = pa.Field(isin=["Dia útil", "Final de semana"])
    Objetivo: Series[str] = pa.Field(isin=["Leads", "Conversão", "Engajamento"])
    Date: Series[str] = pa.Field(str_matches=r"\d{4}-\d{2}-\d{2}")
    AdSet_name: Series[str] = pa.Field(nullable=False)
    Ad_name: Series[str] = pa.Field(nullable=False)
    Amount_spent: Series[str] = pa.Field(nullable=True)
    Link_clicks: Series[float] = pa.Field(ge=0, nullable=True)
    Impressions: Series[int] = pa.Field(ge=0, nullable=True)
    Conversions: Series[int] = pa.Field(ge=0, nullable=True)
    Fase_Funil: Series[str] = pa.Field(nullable=False)
    Segmentacao: Series[str] = pa.Field(nullable=False)
    Tipo_de_Anuncio: Series[str] = pa.Field(isin=["Estático", "Vídeo", "Carrossel"], nullable=False)
    Contexto: Series[str] = pa.Field(nullable=False)
    Fase: Series[str] = pa.Field(nullable=False)

    @pa.check("Organizador", name="unique_organizador", error="Os valores da coluna 'Organizador' devem ser únicos.")
    def unique_organizador(cls, series: Series[int]) -> bool:
        return series.is_unique

# 📌 **Carregar a planilha**
df = pd.read_csv("data/jornada_de_dados_2024.csv")

# 📌 **Validar e capturar os erros**
try:
    LeadFunnelSchema.validate(df, lazy=True)
    print("✅ Planilha validada com sucesso!")
except pa.errors.SchemaErrors as exc:
    print("❌ Erros encontrados na validação!")

    # 📌 Converter erros para JSON estruturado
    errors_dict = exc.failure_cases.to_dict(orient="records")

    # 📌 Caminho do arquivo de saída
    output_file = "validando/validation_errors.json"

    # 📌 Salvar os erros em um arquivo JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(errors_dict, f, indent=4, ensure_ascii=False)


