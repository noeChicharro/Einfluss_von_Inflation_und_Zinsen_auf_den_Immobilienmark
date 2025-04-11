import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/Beschaeftigte_nach_Vollzeitaequivalent_1991-2024.csv')

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS vollzeitaequivalent')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS vollzeitaequivalent (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quartal VARCHAR(10),
    jahr INT,
    bergbau_sek2 FLOAT,
    verarbeitendes_gewerbe_sek2 FLOAT,
    herstellung_nahrungsmittel_sek2 FLOAT,
    herstellung_textilien_sek2 FLOAT,
    herstellung_holzwaren_sek2 FLOAT,
    kokerei_sek2 FLOAT,
    herstellung_pharmaeutika_sek2 FLOAT,
    herstellung_kunststoffe_sek2 FLOAT,
    herstellung_metall_sek2 FLOAT,
    herstellung_datenverarb_geraete_sek2 FLOAT,
    herstellung_elektr_sek2 FLOAT,
    maschinenbau_sek2 FLOAT,
    fahrzeugbau_sek2 FLOAT,
    herstellung_sonstiges_sek2 FLOAT,
    energieversorgung_sek2 FLOAT,
    wasserversorgung_sek2 FLOAT,
    baugewerbe_sek2 FLOAT,
    hoch_tiefbau_sek2 FLOAT,
    sonstiges_asubaugewerbe_sek2 FLOAT,
    kraftfahrzeuge_sek3 FLOAT,
    motorfahrzeuge_sek3 FLOAT,
    grosshande_sek3 FLOAT,
    detailhande_sek3 FLOAT,
    verkehr_sek3 FLOAT,
    landverkehr_sek3 FLOAT,
    schifffahrt_sek3 FLOAT,
    lagerei_sek3 FLOAT,
    postdienste_sek3 FLOAT,
    gastgewerbe_sek3 FLOAT,
    beherbergung_sek3 FLOAT,
    gastronomie_sek3 FLOAT, 
    information_kommunikation_sek3 FLOAT,
    wirtschaftspruefung_sek3 FLOAT,
    telekommunikation_sek3 FLOAT,
    informationstechnologische_informationsdienstl_sek3 FLOAT,  
    finanz_versicherungsdienstl_sek3 FLOAT,
    erbringung_finanzdienstleistungen_sek3 FLOAT,
    versicherungen_sek3 FLOAT,
    versicherungsdienstl_taetigk_sek3 FLOAT,
    grundstuecks_wohnungswesen_sek3 FLOAT,
    freiberufliche_dienstleistungen_sek3 FLOAT,
    wirtschaftspruefung_sek3 FLOAT,
    unternehmensberatung_sek3 FLOAT,
    architektur_ingenieur_sek3 FLOAT,
    forschung_entwicklung_sek3 FLOAT,
    sonstige_freiberufl_dienstleistungen_sek3 FLOAT,
    sonstigen_dienstl_sek3 FLOAT,
    sonstigen_dienstl2_sek3 FLOAT,
    vermittlung_arbeitskraefte_sek3 FLOAT,
    oeffentliche_verwaltung_sek3 FLOAT,
    erziehung_unterricht_sek3 FLOAT,
    gesundheits_sozialwesen_sek3 FLOAT,
    gesundheitswesen_sek3 FLOAT,
    heime_sek3 FLOAT,
    sozialwesen_sek3 FLOAT,
    kunst_sek3 FLOAT,
    sonstige_dienstleistungen_total_sek3 FLOAT
)
'''
cursor.execute(create_value_tabel)
print('Table created')

##data.to_sql('vollzeitaequivalent', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()