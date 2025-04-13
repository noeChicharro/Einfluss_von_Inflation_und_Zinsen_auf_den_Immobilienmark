import pandas as pd
from sqlalchemy import create_engine

## NOCH NICHT MACHEN. HAT EINEN FEHLER xD

engine = create_engine('mysql+mysqlconnector://root:RealMadrid1902!@localhost/bina', echo=False)

data = pd.read_csv('data/Landesindex der Konsumentenpreise_LIK 1914-2025.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS konsumentenpreise')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS konsumentenpreise (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Jahr INT,
    Basis_Datum DATE,
    Landesindex_der_Konsumentenpreise FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('konsumentenpreise', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
