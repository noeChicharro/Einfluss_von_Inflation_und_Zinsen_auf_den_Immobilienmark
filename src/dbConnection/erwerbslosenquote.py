import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/Erwerbslosenquote_gemäss ILO_Grossregionen_2002-2024.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS erwerbslosenquote')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS erwerbslosenquote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Jahr INT,
    Maenner_Genferseeregion FLOAT,
    Maenner_Espace_Mitelland FLOAT,
    Maenner_Nordwestschweiz FLOAT,
    Maenner_Zuerich FLOAT,
    Maenner_Ostschweiz FLOAT,
    Maenner_Zentralschweiz FLOAT,
    Maenner_Tessin FLOAT,
    Frauen_Genferseeregion FLOAT,
    Frauen_Espace_Mitelland FLOAT,
    Frauen_Nordwestschweiz FLOAT,
    Frauen_Zuerich FLOAT,
    Frauen_Ostschweiz FLOAT,
    Frauen_Zentralschweiz FLOAT,
    Frauen_Tessin FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

##data.to_sql('erwerbslosenquote', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
