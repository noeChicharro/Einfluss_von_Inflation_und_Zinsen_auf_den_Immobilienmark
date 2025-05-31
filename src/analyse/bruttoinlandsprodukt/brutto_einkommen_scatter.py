import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np
from dataService import dfCommonBipEinkommen

plt.figure(figsize=(8, 6))
plt.scatter(dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'], dfCommonBipEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], color='mediumseagreen')
plt.xlabel('BIP pro Kopf (CHF)')
plt.ylabel('Haushaltseinkommen (CHF)')
plt.title('Zusammenhang zwischen BIP pro Kopf und Haushaltseinkommen')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show() 

m, b = np.polyfit(dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'], dfCommonBipEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], 1)
plt.plot(dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'], m*dfCommonBipEinkommen['bip_pro_Kopf_CHF_laufende_Preise'] + b, color='gray', linestyle='--')

plt.tight_layout()