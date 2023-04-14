import pandas as pd

pd.read_csv("/output/atp_rankings_90s.csv").to_parquet(
    "/output/pandas_atp_rankings.parquet")
