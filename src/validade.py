import pandera as pa
from pandera import Column, DataFrameSchema, Check

schema = DataFrameSchema({
    "Organizador": Column(int, Check.ge(0), nullable=False),
    "Ano/Mes": Column(str, Check.str_matches(r"\d{4} \| [A-Za-z]+")),
    "Dia da Semana": Column(str, Check.isin(["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"])),
    "Tipo Dia": Column(str, Check.isin(["Dia útil", "Final de semana", "Feriado"])),
    "Objetivo": Column(str),
    "Date": Column(pa.DateTime),
    "AdSet name": Column(str),
    "Ad name": Column(str),
    "Amount spent": Column(str, nullable=True),
    "Link clicks": Column(int, Check.ge(0), nullable=True),
    "Impressions": Column(int, Check.ge(0), nullable=True),
    "Conversions": Column(int, Check.ge(0), nullable=True),
    "Fase Funil": Column(str),
    "Segmentação": Column(str),
    "Tipo de Anúncio": Column(str),
    "Formato do Anúncio": Column(str),
    "Contexto": Column(str),
    "Fase": Column(str),
})

def validar_dados(df):
    try:
        schema.validate(df, lazy=True)
        return None
    except pa.errors.SchemaErrors as err:
        return err.failure_cases
