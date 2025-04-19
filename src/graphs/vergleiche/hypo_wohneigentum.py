from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as matplot

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectHypo = """
    SELECT jahr, monat, festhypo_mittelwert
    FROM hypozinssatz
"""
selectWohn = """
    SELECT jahr, quartal, total
    FROM wohneigentum
"""

cursor.execute(selectHypo)
cursor.execute(selectWohn)
cursor.close()

dfHypo = pd.read_sql(selectHypo, engine)
dfWohn = pd.read_sql(selectWohn, engine)
print(dfHypo.head())
print(dfWohn.head())
engine.dispose()

## durchschnitt aller monatlichen/quartals werte
dfHypo_yearly = dfHypo.groupby('jahr')['festhypo_mittelwert'].mean().reset_index()
dfWohn_yearly = dfWohn.groupby('jahr')['total'].mean().reset_index()
print(dfHypo_yearly.head())
print(dfWohn_yearly.head())

## gemeinsame jahre
dfCommon = pd.merge(dfHypo_yearly, dfWohn_yearly, on='jahr')
print(dfCommon.head())

plt.figure(figsize=(10, 5))

figure, axis1 = plt.subplots(figsize=(10, 5))
color1 = 'tab:blue'
color2 = 'tab:orange'
axis1.set_xlabel('Jahr')
axis1.set_ylabel('Festhypothek Mittelwert', color=color1)
axis1.plot(dfCommon['jahr'], dfCommon['festhypo_mittelwert'], label='Festhypothek Mittelwert', marker='o', color=color1)
axis1.tick_params(axis='y', labelcolor=color1)

axis2 = axis1.twinx()  
axis2.set_ylabel('Wohneigentum Total', color=color2)
axis2.plot(dfCommon['jahr'], dfCommon['total'], label='Wohneigentum Total', marker='s', color=color2)
axis2.tick_params(axis='y', labelcolor=color2)
figure.tight_layout()
plt.title('Festhypothek Mittelwert vs Wohneigentum Total')
plt.grid(True)
plt.show()

## normalized values
dfCommon['festhypo_mittelwert'] = dfCommon['festhypo_mittelwert'] / dfCommon['festhypo_mittelwert'].max()
dfCommon['total'] = dfCommon['total'] / dfCommon['total'].max()
plt.plot(dfCommon['jahr'], dfCommon['festhypo_mittelwert'], label='Festhypothek Mittelwert normalisiert', marker='o', color='royalblue')
plt.plot(dfCommon['jahr'], dfCommon['total'], label='Wohneigentum Total normalisiert', marker='s', color='orange')

plt.title('Festhypothek Mittelwert vs Wohneigentum Total')
plt.xlabel('Jahr')
plt.ylabel('Relativer Wert')
plt.legend()
plt.grid(True)
plt.show() 

