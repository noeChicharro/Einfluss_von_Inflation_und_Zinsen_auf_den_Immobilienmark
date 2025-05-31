import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonBipWohn

plt.figure(figsize=(12, 6))

plt.barh(dfCommonBipWohn['jahr'], dfCommonBipWohn['total'], color='steelblue', label='Wohneigentum')

plt.barh(dfCommonBipWohn['jahr'], -dfCommonBipWohn['bip_pro_Kopf_CHF_laufende_Preise'], color='salmon', label='BIP pro Kopf')

plt.axvline(0, color='black')  
plt.xlabel('Wert')
plt.ylabel('Jahr')
plt.title('Vergleich Wohneigentum und BIP pro Kopf')
plt.legend()
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()