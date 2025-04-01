import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/Bruttoinlandprodukt_pro_Kopf_1991-2023.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS bruttoinlandprodukt (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    bip_pro_Kopf_CHF_laufende_Preise FLOAT,
    veraenderung_VJ_laufende_Preise FLOAT,
    index1991_100_laufende_Preise FLOAT,    
    bip_pro_Kopf_Veraenderung_VJ_Preise_Vorjahr FLOAT,
    index1991_100_Preise_Vorjahr FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('bruttoinlandprodukt', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
