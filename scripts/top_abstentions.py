import pandas as pd
from janitor import clean_names
import src

src.raw_to_bronze(input_dir='data\\raw', output_dir='data\\bronze', pattern='*.zip')

df = pd.read_csv(
    filepath_or_buffer='data\\bronze\\comparecimento_abstencao.csv',
    delimiter=';',
    encoding='latin_1'
)

df = clean_names(df)

df.info()

df \
    .groupby('municipio') \
    .agg(
        total_abs = ('quantidade_de_eleitores_abstencao', 'sum'),
        total_com = ('quantidade_de_eleitores_comparecimento', 'sum'),
        total_apt = ('quantidade_de_eleitores_aptos', 'sum')
        ) \
    .reset_index() \
    .assign(perc_abs = lambda x: x['total_abs'] / x['total_com'])