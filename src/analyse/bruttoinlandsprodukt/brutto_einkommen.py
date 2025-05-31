import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonBipEinkommen

# Linechart
plt.figure(figsize=(12, 6))
plt.plot(dfCommonBipEinkommen['jahr'], dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'], label='BIP pro Kopf', color='steelblue', marker='o')
plt.plot(dfCommonBipEinkommen['jahr'], dfCommonBipEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], label='Haushaltseinkommen', color='salmon', marker='o')

plt.xlabel('Jahr')
plt.ylabel('CHF')
plt.title('BIP pro Kopf vs. Haushaltseinkommen über die Jahre')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

