import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/Haushaltseinkommen und -ausgaben Schweiz_2006-2022.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS haushaltseinkommen')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS haushaltseinkommen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Jahr INT,
    Einkommen_unselbstaendige_Erwerbstaetigkeit varchar(10),    
    Einkommen_selbstaendige_Erwerbstaetigkeit varchar(10),
    Renten_AHV_IV varchar(10),
    Renten_BVG varchar(10),
    Sozialleistungen_Taggelder varchar(10),
    Sozialversicherungsbeitraege varchar(10),
    Steuern varchar(10),
    Krankenkassen_Praemien_Grundversicherung varchar(10),
    Krankenkassen_Praemien_Zusatzversicherungen varchar(10),
    Uebrige_Versicherungspraemien varchar(10),
    Gebuehren varchar(10),
    Spenden_Geschenke_Einladungen varchar(10),
    Nahrungsmittel_alkoholfreie_Getraenke varchar(10),
    Alkoholische_Getraenke_Tabakwaren varchar(10),
    Gast_Beherbergungsstaetten varchar(10),
    Bekleidung_Schuhe varchar(10),
    Wohnen_Energie varchar(10),
    Wohnungseinrichtung_Haushaltsfuehrung varchar(10),
    Gesundheitsausgaben varchar(10),
    Verkehr varchar(10),
    Nachrichtenuebermittlung varchar(10),
    Unterhaltung_Erholung_Kultur varchar(10),
    Andere_Waren_Dienstleistungen varchar(10),
    Anzahl_Selbstaendigerwerbende varchar(10),
    Anzahl_Unselbstaendigerwerbende varchar(10),   
    Anzahl_Rentner varchar(10), 
    Anzahl_Personen_in_Ausbildung varchar(10),
    Anzahl_andere varchar(10),
    Anzahl_KinderU15J varchar(10),
    Anzahl_PersonenU5J varchar(10),
    Anzahl_Personen5bis14J varchar(10),
    Anzahl_Personen_15bis24J varchar(10),
    Anzahl_Personen25bis34 varchar(10),
    Anzahl_Personen35bis44J varchar(10),
    Anzahl_Personen45bis54J varchar(10),
    Anzahl_Personen55bis64J varchar(10),
    Anzahl_Personen65bis74J varchar(10),
    Anzahl_PersonenUE75J varchar(10),
    Anteil_Einpersonenhaushalte varchar(10),
    Anteil_Mieterhaushalte varchar(10),
    Anteil_Rentnerhaushalte varchar(10),
    Anteil_Haushalte_mit_mindestens_1Auto varchar(10),
    Anteil_Haushalte_mit_mindestens_1Velo varchar(10),
    Anteil_Haushalte_mit_mindestens_1Computer varchar(10),
    Anteil_Haushalte_mit_mindestens_1Mobiltelefon varchar(10),  
    Anteil_Haushalte_mit_mindestens_1Haustier varchar(10)
)
'''

cursor.execute(create_value_tabel)
print('Table created')

##data.to_sql('haushaltseinkommen', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
