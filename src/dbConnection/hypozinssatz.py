import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/hypozinssatz_2009-2024.csv', sep=';', encoding='utf-8')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS hypozinssatz')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS hypozinssatz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    monat INT,
    festhypo_mittelwert FLOAT,
    festhypo_median FLOAT,
    festhypo_anzahl_abschluesse FLOAT,    
    variabelhypo_mittelwert FLOAT,
    variabelhypo_median FLOAT,
    variabelhypo_anzahl_abschluesse FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('hypozinssatz', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()