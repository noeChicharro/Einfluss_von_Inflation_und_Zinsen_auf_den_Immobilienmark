import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHiveOther
import matplotlib.pyplot as plt

print(dfDataHiveOther['room_count'])
# Count occurrences of each room count (excluding NaN)
room_counts = dfDataHiveOther['room_count'].value_counts().sort_index()

# Plot pie chart
plt.figure(figsize=(10, 10))
plt.pie(room_counts, labels=room_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Room Counts')
plt.axis('equal')  # Equal aspect ratio ensures pie is a circle.
plt.show()