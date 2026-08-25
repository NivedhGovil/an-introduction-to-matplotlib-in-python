"""Section 7 — Tips and further reading (example.py)

Helpful snippets for saving figures, adjusting figure size, and using subplots.
"""

import matplotlib.pyplot as plt
import numpy as np

# Example: create a simple plot and save it to disk
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)

# Save the current figure to a PNG file with 300 DPI and tight bounding box
plt.savefig("sine_plot.png", dpi=300, bbox_inches="tight")

# Close the figure if running multiple scripts to avoid overlapping figures
plt.close()

# Example: create a 2x2 grid of subplots for multiple related plots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# axes is a 2x2 NumPy array of Axes objects; we can fill them individually
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x), "r")
axes[0, 1].set_title("cos(x)")

axes[1, 0].plot(x, np.tan(x), ".")
axes[1, 0].set_title("tan(x)")

axes[1, 1].plot(x, np.sin(2 * x), "g--")
axes[1, 1].set_title("sin(2x)")

# Tight layout makes sure titles/labels don't overlap
fig.tight_layout()

# Show the figure with all subplots
plt.show()