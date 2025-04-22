import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfGemeindetypen
import matplotlib.pyplot as plt
import squarify

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

plt.figure(figsize=(10, 6))
squarify.plot(sizes=dfGemeindetypen[''], label=dfGemeindetypen['gemeinde'], color=colors, alpha=0.8)
plt.axis('off')
plt.title("Wohneigentum in Gemeindetypen")
plt.show()