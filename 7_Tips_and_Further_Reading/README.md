# Section 7 — Tips and further reading

This final section provides common tips for saving figures, adjusting figure size, and using subplots. It also links to the official Matplotlib documentation.

Example tips (see example.py in this folder for commented usage):

```python
# Save figure to disk with high DPI and tight layout
plt.savefig("figure.png", dpi=300, bbox_inches="tight")

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Use the gallery and docs for more advanced topics: https://matplotlib.org
```

Further reading:
- Matplotlib official documentation: https://matplotlib.org
- Matplotlib gallery for examples and inspiration.