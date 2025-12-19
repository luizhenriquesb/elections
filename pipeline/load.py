import pandas as pd
import src
import duckdb 
from pathlib import Path

# List of csv files (landing) 
files = list(Path('data\\landing').rglob('*.csv'))

# DuckDB connection
con = duckdb.connect('data\\lakehouse.duckdb', read_only=False)

# Check tables
con.query('SHOW TABLES')

# ==============================
# 1. 'comparecimento_abstencao'
## Read files
com_abs = pd.concat(
    [src.read_tse(file) for file in files if file.stem.endswith('comparecimento_abstencao')],
    ignore_index=True
    )

## Insert into DuckDB 
con.execute('CREATE OR REPLACE TABLE source_comparecimento_abstencao AS SELECT * FROM com_abs')

# 2. 'votacao_candidato'
## Read files
vot_can = pd.concat(
    [src.read_tse(file) for file in files if file.stem.endswith('votacao_candidato')]
    )

## Insert into DuckDB 
con.execute('CREATE OR REPLACE TABLE source_votacao_candidato AS SELECT * FROM vot_can')
# ==============================

# Check tables
con.query('SHOW TABLES')
con.query("DESCRIBE source_comparecimento_abstencao")
con.query("DESCRIBE source_votacao_candidato")

# Disconnect
con.interrupt()
