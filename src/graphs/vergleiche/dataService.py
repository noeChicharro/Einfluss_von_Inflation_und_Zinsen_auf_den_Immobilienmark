from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

# Inflationsrate
selectLik = """
    SELECT Jahr, lik, hvpi
    FROM inflationsrate
"""

# Wohneigentum
selectWohn = """
    SELECT jahr, quartal, total, gemeindetyp_1, gemeindetyp_2, gemeindetyp_3, gemeindetyp_4, gemeindetyp_5
    FROM wohneigentum
"""

# Haushaltseinkommen
selectEinkommen = """
    SELECT Jahr, Einkommen_unselbstaendige_Erwerbstaetigkeit
    FROM haushaltseinkommen
"""

# Bruttoinlandprodukt
selectBrutto = """
    SELECT jahr, bip_pro_Kopf_CHF_laufende_Preise
    FROM bruttoinlandprodukt
"""

# Hypothekenzinssatz
selectHypo = """
    SELECT jahr, monat, festhypo_mittelwert
    FROM hypozinssatz
"""

cursor.execute(selectLik)
cursor.execute(selectWohn)
cursor.execute(selectEinkommen)
cursor.execute(selectBrutto)
cursor.execute(selectHypo)
cursor.close()

dfLik = pd.read_sql(selectLik, engine)
dfWohn = pd.read_sql(selectWohn, engine)
dfEinkommen = pd.read_sql(selectEinkommen, engine)
dfBrutto = pd.read_sql(selectBrutto, engine)
dfHypo = pd.read_sql(selectHypo, engine)

engine.dispose()

## Strings zu numerischen Werten umwandeln
dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = (
    dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit']
    .str.replace("'", '', regex=False)    
    .str.replace(",", '.', regex=False)    
    .str.replace(" ", '', regex=False)    
)
dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = pd.to_numeric(dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], errors='coerce')


## Gemeindetypen Jahresdruchschnitt
## durchschnitt aller monatlichen/quartals werte
dfGemeinde1_yearly = dfWohn.groupby('jahr')['gemeindetyp_1'].mean().reset_index()
dfGemeinde2_yearly = dfWohn.groupby('jahr')['gemeindetyp_2'].mean().reset_index()
dfGemeinde3_yearly = dfWohn.groupby('jahr')['gemeindetyp_3'].mean().reset_index()
dfGemeinde4_yearly = dfWohn.groupby('jahr')['gemeindetyp_4'].mean().reset_index()
dfGemeinde5_yearly = dfWohn.groupby('jahr')['gemeindetyp_5'].mean().reset_index()

dfGemeindetypen = dfGemeinde1_yearly.copy()
dfGemeindetypen = dfGemeindetypen.rename(columns={'gemeindetyp_1': 'Typ 1'}) ## Städtische Gemeinde einer kleinen Agglomeration
dfGemeindetypen['Typ 2'] = dfGemeinde2_yearly['gemeindetyp_2'] ## Städtische Gemeinde einer mittelgrossen Agglomeration 
dfGemeindetypen['Typ 3'] = dfGemeinde3_yearly['gemeindetyp_3'] ## Städtische Gemeinde einer kleinen oder ausserhalb einer Agglomeration 
dfGemeindetypen['Typ 4'] = dfGemeinde4_yearly['gemeindetyp_4'] ## Intermediäre Gemeinde 
dfGemeindetypen['Typ 5'] = dfGemeinde5_yearly['gemeindetyp_5'] ## Ländliche Gemeinde 
 
## Jährlicher Hypothekenzinssatz (Durchschnitt)
dfHypo_yearly = dfHypo.groupby('jahr')['festhypo_mittelwert'].mean().reset_index()

## Jährliches Wohneigentum (Durchschnitt)
dfWohn_yearly = dfWohn.groupby('jahr')['total'].mean().reset_index()

## Common Hypothekenzinssatz und Wohneigentum (jährlich)
dfCommonHypoWohn = pd.merge(dfHypo_yearly, dfWohn_yearly, on='jahr')
dfCommonHypoWohn = dfCommonHypoWohn.sort_values('jahr')

## Common Einkommen und Wohneigentum (jährlich)
dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfWohn = dfWohn[dfWohn['jahr'] >= 2017]
dfEinkommen = dfEinkommen[dfEinkommen['jahr'].isin(dfWohn['jahr'])]
dfCommonWohnEinkommen = pd.merge(dfWohn, dfEinkommen, on='jahr')
dfCommonWohnEinkommen = dfCommonWohnEinkommen.sort_values('jahr')

## Common Wohneigentum und BIP (jährlich)
dfCommonBipWohn = pd.merge(dfWohn.groupby('jahr')['total'].mean().reset_index(), dfBrutto, on='jahr')
dfCommonBipWohn = dfCommonBipWohn.sort_values('jahr') 

## Common Einkommen und BIP (jährlich)
dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfBrutto = dfBrutto[dfBrutto['jahr'] >= 2017]
dfBrutto = dfBrutto[dfBrutto['jahr'].isin(dfBrutto['jahr'])]
dfCommonBipEinkommen = pd.merge(dfBrutto, dfEinkommen, on='jahr')
