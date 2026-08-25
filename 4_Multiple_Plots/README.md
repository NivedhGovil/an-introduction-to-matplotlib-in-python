# Section 4 — Multiple plots and the format shorthand

This short section illustrates the format shorthand (marker|line|color) and shows multiple lines together. Use the shorthand to combine marker, line style, and color in one string.

Example (see example.py for commented version):

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4])
y1 = np.array([1, 4, 9, 16, 25])
y2 = np.array([1, 2, 3, 4, 5])

plt.plot(x, y1, '*--y')  # star markers, dashed line, yellow color
plt.plot(x, y2, 'o-')    # circle markers, solid line, default color
plt.show()
```

When plotting many subplots use plt.subplots() or figure/axes API for fine control.