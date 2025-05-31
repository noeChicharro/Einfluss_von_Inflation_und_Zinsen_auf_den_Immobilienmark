import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonHypoWohn

plt.figure(figsize=(10, 5))

figure, axis1 = plt.subplots(figsize=(10, 5))
color1 = 'tab:blue'
color2 = 'tab:orange'
axis1.set_xlabel('Jahr')
axis1.set_ylabel('Festhypothek Mittelwert', color=color1)
axis1.plot(dfCommonHypoWohn['jahr'], dfCommonHypoWohn['festhypo_mittelwert'], label='Festhypothek Mittelwert', marker='o', color=color1)
axis1.tick_params(axis='y', labelcolor=color1)

axis2 = axis1.twinx()  
axis2.set_ylabel('Wohneigentum Total', color=color2)
axis2.plot(dfCommonHypoWohn['jahr'], dfCommonHypoWohn['total'], label='Wohneigentum Total', marker='s', color=color2)
axis2.tick_params(axis='y', labelcolor=color2)
figure.tight_layout()
plt.title('Festhypothek Mittelwert vs Wohneigentum Total')
plt.grid(True)
plt.show()



