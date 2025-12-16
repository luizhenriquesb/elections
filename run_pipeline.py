import pandas as pd
import duckdb
import src

con = duckdb.connect(database='data\\lakehouse.duckdb', read_only=False)

duckdb.query('SHOW TABLES')

# Extract
src.extract_raw_to_staging(input_dir='data/raw', output_dir='data/staging')
