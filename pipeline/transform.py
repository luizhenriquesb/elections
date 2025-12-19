# Library
import ibis
import src
import pandas as pd

# Connection with database (DuckBD)
con = ibis.duckdb.connect('data\\lakehouse.duckdb', read_only=False)

# Tables
con.list_tables()

# Read data
com = con.table('source_comparecimento_abstencao')
vot = con.table('source_votacao_candidato')

# Clean names
com = src.clean_names(com)
vot = src.clean_names(vot)

### Percent of abstention
com = com \
    .mutate(
        perc = com.quantidade_de_eleitores_abstencao / com.quantidade_de_eleitores_aptos
        )

top_10 = vot \
    .filter(
        vot.municipio == 'SÃO PAULO',
        vot.cargo == 'Prefeito',
        vot.turno == 1, 
        vot.ano_de_eleicao == 2024
    ) \
    .group_by('nome_candidato', 'partido') \
    .aggregate(
        total_validos = vot.votos_validos.sum(),
        total_nominais = vot.votos_nominais.sum()
        ) \
    .execute()

top_10.to_csv('dash_app\\top_10.csv')
