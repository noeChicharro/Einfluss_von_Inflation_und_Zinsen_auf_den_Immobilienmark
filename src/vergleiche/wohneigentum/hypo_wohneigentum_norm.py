import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonHypoWohn

dfCommonHypoWohn['festhypo_mittelwert'] = dfCommonHypoWohn['festhypo_mittelwert'] / dfCommonHypoWohn['festhypo_mittelwert'].max()
dfCommonHypoWohn['total'] = dfCommonHypoWohn['total'] / dfCommonHypoWohn['total'].max()
plt.plot(dfCommonHypoWohn['jahr'], dfCommonHypoWohn['festhypo_mittelwert'], label='Festhypothek Mittelwert normalisiert', marker='o', color='royalblue')
plt.plot(dfCommonHypoWohn['jahr'], dfCommonHypoWohn['total'], label='Wohneigentum Total normalisiert', marker='s', color='orange')

plt.title('Festhypothek Mittelwert vs Wohneigentum Total')
plt.xlabel('Jahr')
plt.ylabel('Relativer Wert')
plt.legend()
plt.grid(True)
plt.show() 