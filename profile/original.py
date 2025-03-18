import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data/jd_original.csv')
profile = ProfileReport(df, title="Profiling Report")
profile.to_file('profile/profile_original.html')