This project aims to analyze electoral data from the [TSE (Superior Electoral Court)](https://www.tse.jus.br/). The basics structure is as follows:
```
elections/
  ├── data/ 
  │   ├── raw/
  │   ├── landing/
  │   └── lakehouse.duckdb/
  |
  ├── dashboard/
  |   ├── app.py
  |   ├── requirements.txt
  |   ├── sharep.py
  │   └── style.css
  │
  ├── pipeline/
  │   ├── extract.py
  │   ├── load.py
  │   └── transform.py
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
