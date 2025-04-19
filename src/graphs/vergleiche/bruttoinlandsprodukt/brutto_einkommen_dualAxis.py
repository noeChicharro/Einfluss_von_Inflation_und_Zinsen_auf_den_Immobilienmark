import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonBipEinkommen

fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.set_xlabel('Jahr')
ax1.set_ylabel('BIP pro Kopf (CHF)', color='steelblue')
ax1.plot(dfCommonBipEinkommen['jahr'], dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'], color='steelblue', marker='o', label='BIP')
ax1.tick_params(axis='y', labelcolor='steelblue')

ax2 = ax1.twinx()
ax2.set_ylabel('Haushaltseinkommen (CHF)', color='salmon')
ax2.plot(dfCommonBipEinkommen['jahr'], dfCommonBipEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], color='salmon', marker='o', label='Einkommen')
ax2.tick_params(axis='y', labelcolor='salmon')

plt.title('BIP pro Kopf und Haushaltseinkommen')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()