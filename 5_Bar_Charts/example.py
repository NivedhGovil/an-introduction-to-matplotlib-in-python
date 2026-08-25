"""Section 5 — Bar charts (example.py)

Creates a simple vertical bar chart and explains figure sizing and color choices.
"""

import numpy as np
import matplotlib.pyplot as plt

# Categories (x-axis) and their corresponding numeric values (heights)
categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy"])
values = np.array([4, 3, 2, 5, 3])

# Set the figure size in inches (width, height)
plt.figure(figsize=(7, 5))

# Draw a vertical bar chart; color can be any Matplotlib color spec
plt.bar(categories, values, color="#a87132")

# Display the plot
plt.show()