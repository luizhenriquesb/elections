import datetime
import pandas as pd
import duckdb
import src
import os
from pathlib import Path
from datetime import datetime
import hashlib

con = duckdb.connect('data\\lakehouse.duckdb', read_only=False)

files = list(Path('data\\staging').rglob('*.csv'))

con.query('SHOW TABLES')
con.execute('DROP TABLE ingestion_log')

con.execute(
    """
    CREATE TABLE ingestion_log (
        id          TEXT PRIMARY KEY,
        etl_stage   TEXT NOT NULL
            CHECK (etl_stage IN ('raw_to_stg', 'stg_to_marts')),
        file_path   TEXT NOT NULL,
        file_name   TEXT NOT NULL,
        dt_loaded   TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        dt_modified TIMESTAMP NOT NULL 
    ) 
    """
)

# id = hashlib.sha256(str(file).encode('utf-8')).hexdigest()
# etl_stage = 'stg'
# file_path = str(file)
# file_name = file.stem
# dt_loaded = pd.NA
# dt_modified = datetime.fromtimestamp(file.stat().st_mtime).replace(microsecond=0)

rows = []

for file in files:

    rows.append(
        (# Metadata
        # id
        hashlib.sha256(str(file).encode('utf-8')).hexdigest(),
        # etl_stage
        'raw_to_stg',
        # file_path
        str(file),
        # file_name
        file.stem,
        # dt_loaded
        # pd.NA,
        # dt_modified
        datetime.fromtimestamp(file.stat().st_mtime).replace(microsecond=0))
    )

rows

con.executemany(
    """
    INSERT OR IGNORE INTO ingestion_log (
        id, etl_stage, file_path, file_name, dt_modified
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    rows,
)

con.query("SELECT * FROM ingestion_log")

