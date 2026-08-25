# Section 6 — Scatter plots and annotations

This section covers scatter plots (point clouds), adding horizontal lines, legends, and labels.

Example (see example.py in this folder for a commented version):

```python
import numpy as np
import matplotlib.pyplot as plt

x1 = [0,1,1,2,3,4,5,6,7,7,8]
y1 = [55,60,65,62,68,70,75,78,82,85,87]

x2 = np.array([0,1,2,2,3,4,5,6,7,8,8])
y2 = np.array([50,58,65,70,72,78,83,88,92,95,97])

plt.scatter(x1, y1, s=50, color="#d11d59", label="Class A")
plt.scatter(x2, y2, s=50, color="#6ba867", label="Class B")

plt.xlabel("Hours studied")
plt.ylabel("Test Scores")
plt.axhline(y=85, color="#4287f5", linestyle="--", label="Marks to get A grade")
plt.legend()
plt.show()
```

Use plt.legend() to show labels provided to plotting calls.