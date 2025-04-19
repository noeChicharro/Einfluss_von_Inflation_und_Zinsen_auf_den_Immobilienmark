import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfGemeindetypen
import matplotlib.pyplot as plt

# Plot
plt.figure(figsize=(12, 6))

highlight = 'Typ 4' 

for col in ['Typ 1', 'Typ 2', 'Typ 3', 'Typ 4', 'Typ 5']:

   ## plt.plot(dfGemeindetypen['jahr'], df_all[col], marker='o', label=col) -> wenn nicht gehilighted werden soll diesen code verwenden und if auskommentieren
    if col == highlight:
        plt.plot(dfGemeindetypen['jahr'], dfGemeindetypen[col], label=col, linewidth=3, color='crimson')
    else:
        plt.plot(dfGemeindetypen['jahr'], dfGemeindetypen[col], label=col, linewidth=1.5, linestyle='--', color='gray')

plt.title('Entwicklung des Wohneigentums über die Jahre')
plt.xlabel('Jahr')
plt.ylabel('Durchschnittlicher Wert')
plt.legend(title='Gemeindetyp')
plt.grid(True)
plt.tight_layout()
plt.show()

highlight = 'Typ 3'

