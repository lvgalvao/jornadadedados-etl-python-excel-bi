# instalando pip install ydata-profiling

from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("data/jornada_de_dados_2024.csv")
profile = ProfileReport(df, explorative=True)
profile.to_file("report.html")
