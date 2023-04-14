import duckdb

con = duckdb.connect(database=':memory:')
con.execute("SET memory_limit='100MB'")
con.execute("""
COPY (SELECT * FROM '/output/atp_rankings_90s.csv')
TO '/output/duck_atp_rankings.parquet'
(FORMAT PARQUET, CODEC 'ZSTD', ROW_GROUP_SIZE 100000);
""")
