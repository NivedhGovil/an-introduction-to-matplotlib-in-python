"""Section 3 — Titles, labels, and ticks (example.py)

This script shows how to set a plot title, axis labels, explicit x ticks, and how to plot multiple series.
Each line includes a comment explaining its purpose.
"""

import matplotlib.pyplot as plt
import numpy as np

# X values represent years and y values are three different class-size series
x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 5])
y3 = np.array([13, 15, 20, 30])

# Add a title with font customizations
plt.title("Class size over the years", fontsize=20, family="serif", fontweight="bold")

# Add axis labels
plt.xlabel("Year", fontsize=15)
plt.ylabel("Class size", fontsize=15)

# Set x-axis tick locations to the years in x
plt.xticks(x)

# Plot three lines on the same axes
plt.plot(x, y1)  # first series
plt.plot(x, y2)  # second series
plt.plot(x, y3)  # third series

# Render the figure
plt.show()