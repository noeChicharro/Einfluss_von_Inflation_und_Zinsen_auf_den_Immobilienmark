import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dataService import dfCommonWohnEinkommen

dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = pd.to_numeric(dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], errors='coerce')
dfCommonWohnEinkommen['wohneigentum_norm'] = dfCommonWohnEinkommen['total'] / dfCommonWohnEinkommen['total'].max()
dfCommonWohnEinkommen['einkommen_norm'] = dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] / dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'].max()
print(dfCommonWohnEinkommen['wohneigentum_norm'])
print(dfCommonWohnEinkommen['einkommen_norm'])

x = np.arange(len(dfCommonWohnEinkommen['jahr']))
width = 0.35

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, dfCommonWohnEinkommen['wohneigentum_norm'], width, label='Wohneigentum (normalisiert)', color='steelblue')
plt.bar(x + width/2, dfCommonWohnEinkommen['einkommen_norm'], width, label='Einkommen (normalisiert)', color='salmon')

plt.xticks(x, dfCommonWohnEinkommen['jahr'])
plt.xlabel('Jahr')
plt.ylabel('Normalisierter Wert (0–1)')
plt.title('Vergleich von Wohneigentum und Einkommen (normalisiert)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()