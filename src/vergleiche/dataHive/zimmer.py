import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHiveOther
import pandas as pd
import matplotlib.pyplot as plt

filtered_data = dfDataHiveOther[dfDataHiveOther['room_count'] <= 10]
room_counts = filtered_data['room_count'].value_counts().sort_index()
room_percentages = (room_counts / room_counts.sum()) * 100

# Filter 0% aus
non_zero_mask = room_percentages > 1
room_counts = room_counts[non_zero_mask]
room_percentages = room_percentages[non_zero_mask]

# Plot pie chart
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(
    room_counts,
    labels=room_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    labeldistance=1.05,
    pctdistance=0.85
)
ax.set_title('Zimmeranzahlverteilung')
ax.axis('equal')
plt.tight_layout()
plt.show()
