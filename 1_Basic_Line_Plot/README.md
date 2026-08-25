# Section 1 — Basic line plot

This section introduces the most basic line plot in Matplotlib. The example shows how to plot y versus x and how Matplotlib uses default x-values when only y is provided.

Example (see example.py in this folder for commented version):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 6])
y = np.array([10, 250])

plt.plot(x, y)
plt.show()
```

Notes:
- If you only pass y values to plt.plot, Matplotlib will assume x = [0, 1, 2, ...].
- Use plt.show() to display the figure (in scripts or interactive sessions).