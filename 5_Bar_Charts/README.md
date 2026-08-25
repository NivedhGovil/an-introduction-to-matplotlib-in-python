# Section 5 — Bar charts

This section shows how to create vertical bar charts and set figure size. For horizontal bars use plt.barh(...).

Example (see example.py in this folder for commented version):

```python
import numpy as np
import matplotlib.pyplot as plt

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy"])
values = np.array([4, 3, 2, 5, 3])

plt.figure(figsize=(7,5))
plt.bar(categories, values, color="#a87132")
plt.show()
```

Bar charts are useful to compare categorical data side-by-side.