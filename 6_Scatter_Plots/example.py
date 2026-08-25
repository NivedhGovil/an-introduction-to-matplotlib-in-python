"""Section 6 — Scatter plots and annotations (example.py)

Creates two scatter series, adds labels, a guide line, and a legend.
Comments explain each parameter.
"""

import numpy as np
import matplotlib.pyplot as plt

# Class A data (lists work fine for scatter)
x1 = [0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]
y1 = [55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]

# Class B data as NumPy arrays
x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

# Scatter plots: s controls marker size, color is a color string/hex, label used by legend
plt.scatter(x1, y1, s=50, color="#d11d59", label="Class A")
plt.scatter(x2, y2, s=50, color="#6ba867", label="Class B")

# Axis labels
plt.xlabel("Hours studied")
plt.ylabel("Test Scores")

# Draw a horizontal reference line at y=85 (e.g., threshold for grade A)
plt.axhline(y=85, color="#4287f5", linestyle="--", label="Marks to get A grade")

# Show legend to identify each series
plt.legend()

# Render the figure
plt.show()