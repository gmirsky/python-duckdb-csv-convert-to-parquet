import polars as pl

pl.scan_csv("/output/atp_rankings_90s.csv").sink_parquet(
    "/output/polars_atp_rankings.parquet",
    compression="zstd",
    row_group_size=100_000
)
