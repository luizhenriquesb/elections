# Library
import ibis

# Connection with database (DuckBD)
con = ibis.duckdb.connect('data\\lakehouse.duckdb', read_only=False)

# Read data
com = con.table('source_comparecimento_abstencao')
vot = con.table('source_votacao_candidato')

### Candidates with the most votes

# Group by and aggregates
vot_agg = vot \
    .filter(vot.turno == 1, vot.cargo != "Prefeito") \
    .group_by(['municipio', 'nome_candidato', 'numero_candidato', 'partido']) \
    .aggregate(total_nominal_votes = vot.votos_nominais.sum())

# Creates a window
w = ibis.window(order_by=ibis.desc('total_nominal_votes'), group_by='municipio')

# Adds a rank column
vot_ranked = vot_agg.mutate(rank=ibis.row_number().over(w))
vot_ranked.filter(vot_ranked.municipio == 'SÃO PAULO').execute()

# Filter just the most voted
most_voted = vot_ranked.filter(vot_ranked.rank == 0)

# See the result
most_voted.execute().sort_values(by='total_nominal_votes', ascending=False)