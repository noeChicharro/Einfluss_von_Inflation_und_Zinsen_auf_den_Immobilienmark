import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/durchschnittliche_Jahresteuerung_2017_2024.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS jahressteuern')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS jahressteuern (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    grossen_Agglomeration FLOAT,
    mittelgrossen_Agglomeration FLOAT,
kleinen_Agglomeration FLOAT,
    intermediaere_Gemeinde FLOAT,
    laendliche_Gemeinde FLOAT,
    EFH_grossen_Agglomeration FLOAT,
    EFH_mittelgrossen_Agglomeration FLOAT,
    EFH_kleinen_Agglomeration FLOAT,
    EFH_Intermediaere_Gemeinde FLOAT,
    EFH_laendliche_Gemeinde FLOAT,
    EGW_grossen_Agglomeration FLOAT,
    EGW_mittelgrossen_Agglomeration FLOAT,
    EGW_kleinen_Agglomeration FLOAT,
    EGW_Intermediaere_Gemeinde FLOAT,
    EGW_laendliche_Gemeinde FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('jahressteuern', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
