import pandas as pd
from ydata_profiling import ProfileReport

def main(DATA_PATH, PROFILE_PATH):
    df = pd.read_csv(DATA_PATH)
    profile = ProfileReport(df, title="Profiling Report")
    profile.to_file(PROFILE_PATH)
    print(f"Profiling report saved to {PROFILE_PATH}")

if __name__ == "__main__":
    DATA_PATH = 'data/jd_original.csv'
    PROFILE_PATH = 'profile/jd_original.html'
    main(DATA_PATH, PROFILE_PATH)