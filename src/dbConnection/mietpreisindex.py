import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../../data/landesindex_der_konsumentenpreise_wohnungsmiete_jahresdurchschnitte_1940_2024.csv')

data['basisdatum'] = data['basisdatum'].str.replace('00:00:00', '')
data['basisdatum'] = data['basisdatum'].str.replace(r'\s+', '')

cursor = engine.cursor()

cursor.execute('DROP TABLE IF EXISTS valueYear')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS mietpreisindex (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    basisdatum DATE,
    indexwert FLOAT
)
'''

##data.to_sql('mietpreisindex', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

engine.cursor.close()
