from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectBrutto = """
    SELECT jahr, bip_pro_Kopf_CHF_laufende_Preise
    FROM bruttoinlandprodukt
"""

selectEinkommen = """
    SELECT Jahr, Einkommen_unselbstaendige_Erwerbstaetigkeit
    FROM haushaltseinkommen
"""
cursor.execute(selectBrutto)
cursor.execute(selectEinkommen)
cursor.close()

dfBrutto = pd.read_sql(selectBrutto, engine)
dfEinkommen = pd.read_sql(selectEinkommen, engine)
print(dfEinkommen.head(), dfBrutto.head())
engine.dispose()

dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfBrutto = dfBrutto[dfBrutto['jahr'] >= 2017]
dfBrutto = dfBrutto[dfBrutto['jahr'].isin(dfBrutto['jahr'])]
df_merged = pd.merge(dfBrutto, dfEinkommen, on='jahr')
print(df_merged.head())

df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = (
    df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit']
    .str.replace("'", '', regex=False)    
    .str.replace(",", '.', regex=False)    
    .str.replace(" ", '', regex=False)    
)
df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = pd.to_numeric(df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], errors='coerce')

# Linechart
plt.figure(figsize=(12, 6))
plt.plot(df_merged['jahr'], df_merged['bip_pro_Kopf_CHF_laufende_Preise'], label='BIP pro Kopf', color='steelblue', marker='o')
plt.plot(df_merged['jahr'], df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], label='Haushaltseinkommen', color='salmon', marker='o')

plt.xlabel('Jahr')
plt.ylabel('CHF')
plt.title('BIP pro Kopf vs. Haushaltseinkommen über die Jahre')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Dual Axis Plot
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Jahr')
ax1.set_ylabel('BIP pro Kopf (CHF)', color='steelblue')
ax1.plot(df_merged['jahr'], df_merged['bip_pro_Kopf_CHF_laufende_Preise'], color='steelblue', marker='o', label='BIP')
ax1.tick_params(axis='y', labelcolor='steelblue')

ax2 = ax1.twinx()
ax2.set_ylabel('Haushaltseinkommen (CHF)', color='salmon')
ax2.plot(df_merged['jahr'], df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], color='salmon', marker='o', label='Einkommen')
ax2.tick_params(axis='y', labelcolor='salmon')

plt.title('BIP pro Kopf und Haushaltseinkommen')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(df_merged['bip_pro_Kopf_CHF_laufende_Preise'], df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], color='mediumseagreen')
plt.xlabel('BIP pro Kopf (CHF)')
plt.ylabel('Haushaltseinkommen (CHF)')
plt.title('Zusammenhang zwischen BIP pro Kopf und Haushaltseinkommen')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show() 

# Optional: add a regression line
m, b = np.polyfit(df_merged['bip_pro_Kopf_CHF_laufende_Preise'], df_merged['Einkommen_unselbstaendige_Erwerbstaetigkeit'], 1)
plt.plot(df_merged['bip_pro_Kopf_CHF_laufende_Preise'], m*df_merged['bip_pro_Kopf_CHF_laufende_Preise'] + b, color='gray', linestyle='--')

plt.tight_layout()
