from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectWohn = """
    SELECT jahr, quartal, total
    FROM wohneigentum
"""

selectEinkommen = """
    SELECT Jahr, Einkommen_unselbstaendige_Erwerbstaetigkeit
    FROM haushaltseinkommen
"""
cursor.execute(selectWohn)
cursor.execute(selectEinkommen)
cursor.close()

dfWohn = pd.read_sql(selectWohn, engine)
dfEinkommen = pd.read_sql(selectEinkommen, engine)
dfWohn = dfWohn.groupby('jahr')['total'].mean().reset_index()
print(dfWohn.head(), dfEinkommen.head())
engine.dispose()

dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfWohn = dfWohn[dfWohn['jahr'] >= 2017]
dfEinkommen = dfEinkommen[dfEinkommen['jahr'].isin(dfWohn['jahr'])]
df_merged = pd.merge(dfWohn, dfEinkommen, on='jahr')
print(df_merged.head())


x = np.arange(len(df_merged['jahr']))  
width = 0.35  

plt.figure(figsize=(12, 6))

plt.bar(x - width/2, df_merged['total'], width, label='Wohneigentum', color='steelblue')
plt.bar(x + width/2, df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], width, label='Einkommen', color='salmon')

plt.xticks(x, df_merged['jahr'])
plt.xlabel('Jahr')
plt.ylabel('Wert')
plt.title('Vergleich von Wohneigentum und Einkommen ab 2017')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

## Dual Axis Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Wohneigentum on left axis
ax1.bar(df_merged['jahr'], df_merged['total'], width=0.4, align='edge', color='steelblue', label='Wohneigentum')
ax1.set_ylabel('Wohneigentum (CHF)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

# Einkommen on right axis
ax2 = ax1.twinx()
ax2.bar(df_merged['jahr'], df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], width=-0.4, align='edge', color='salmon', label='Einkommen')
ax2.set_ylabel('Einkommen (CHF)', color='salmon')
ax2.tick_params(axis='y', labelcolor='salmon')

plt.title('Wohneigentum vs. Einkommen (Dual-Axis)')
plt.xticks(df_merged['jahr'])
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


## Normalisierung
## convert columns to numeric
df_merged['total'] = pd.to_numeric(df_merged['total'], errors='coerce')
df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = (
    df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit']
    .str.replace("'", '', regex=False)    
    .str.replace(",", '.', regex=False)    
    .str.replace(" ", '', regex=False)    
)
df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = pd.to_numeric(df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], errors='coerce')
df_merged['wohneigentum_norm'] = df_merged['total'] / df_merged['total'].max()
df_merged['einkommen_norm'] = df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'] / df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'].max()
print(df_merged['wohneigentum_norm'])
print(df_merged['einkommen_norm'])

x = np.arange(len(df_merged['jahr']))
width = 0.35

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, df_merged['wohneigentum_norm'], width, label='Wohneigentum (normalisiert)', color='steelblue')
plt.bar(x + width/2, df_merged['einkommen_norm'], width, label='Einkommen (normalisiert)', color='salmon')

plt.xticks(x, df_merged['jahr'])
plt.xlabel('Jahr')
plt.ylabel('Normalisierter Wert (0–1)')
plt.title('Vergleich von Wohneigentum und Einkommen (normalisiert)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()