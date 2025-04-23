import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/impi_wohneigentum_ 2017-2024.csv', sep=';', encoding='utf-8')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS wohneigentum')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS wohneigentum (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quartal VARCHAR(10),
    jahr INT,
    total FLOAT,
    gemeindetyp_1 FLOAT,
    gemeindetyp_2 FLOAT,    
    gemeindetyp_3 FLOAT,
    gemeindetyp_4 FLOAT,
    gemeindetyp_5 FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('wohneigentum', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()