This project aims to analyze electoral data from the [TSE (Superior Electoral Court)](https://www.tse.jus.br/). The basics structure is as follows:
```
elections/
  ├── data/ 
  │   ├── raw/
  │   ├── stage/
  │   ├── marts/
  │   └── lakehouse.duckdb/
  │
  ├── pipeline/
  │   ├── extract/
  │   ├── load/
  │   └── transform/
  │
  ├── src/
  │   ├── __init__.py
  │   ├── extract/
  │   └── load/ 
  │
  ├── tests/ 
  │
  ├── .venv
  ├── .gitignore
  └── requirements.txt 
```
