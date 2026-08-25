"""Section 1 — Basic line plot (example.py)

This script demonstrates a minimal line plot and explains each step.
"""

# Import matplotlib for plotting and numpy for numerical arrays
import matplotlib.pyplot as plt
import numpy as np

# Define x and y data as NumPy arrays
x = np.array([0, 6])  # x coordinates for two points
y = np.array([10, 250])  # corresponding y coordinates

# Plot y versus x as a line
plt.plot(x, y)  # draws a line connecting (0,10) and (6,250)

# Display the plot window (required to render the figure in scripts)
plt.show()