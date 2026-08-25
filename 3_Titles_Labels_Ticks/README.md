# Section 3 — Titles, labels, and ticks

This section explains how to add a title, axis labels, and control tick locations. It also shows plotting multiple series on the same axes.

Example (see example.py in this folder for commented version):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,38,5])
y3 = np.array([13,15,20,30])

plt.title("Class size over the years", fontsize=20, family="serif", fontweight="bold")
plt.xlabel("Year", fontsize=15)
plt.ylabel("Class size", fontsize=15)

plt.xticks(x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()
```

Use plt.xticks(...) to set tick locations explicitly. Titles and labels accept font size and family options.