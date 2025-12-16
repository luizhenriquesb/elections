from pathlib import Path
import pandas as pd

def read_tse(path: Path):
    df = pd.read_csv(filepath_or_buffer=path, encoding='latin_1', delimiter=';')
    return df
