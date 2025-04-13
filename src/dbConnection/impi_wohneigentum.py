import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

engine = create_engine('mysql+mysqlconnector://root:WhrAikre4xqhECNyjB8j@localhost/bina', echo=False)

# Bestimme das Verzeichnis dieser Datei (also hypozinssatz.py)
base_path = Path(__file__).resolve().parent

# Gehe zwei Ebenen nach oben zum Projektverzeichnis und dann in den Ordner 'data'
csv_path = base_path / '..' / '..' / 'data' / 'impi_wohneigentum_2017-2024.csv'

# Konvertiere in absoluten Pfad
csv_path = csv_path.resolve()

# Lies die CSV-Datei mit relativem Pfad ein
data = pd.read_csv(csv_path)

# Beispiel: Gib die ersten Zeilen aus
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS impi_wohneigentum')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS impi_wohneigentum (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr_quartal varchar(10),
    total FLOAT, 
    gemeindetyp_1 FLOAT, 
    gemeindetyp_2 FLOAT,
    gemeindetyp_3 FLOAT,
    gemeindetyp_4 FLOAT,
    gemeindetyp_5 FLOAT
);
'''

cursor.execute(create_value_tabel)
print('Table created')

##data.to_sql('erwerbslosenquote', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()