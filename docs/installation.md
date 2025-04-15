# Installation Guide

This guide will help you install and set up the Math Art library.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation Methods

### From PyPI (Recommended)

```bash
pip install math-art
```

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/math-art.git
   cd math-art
   ```

2. Install the package:
   ```bash
   pip install -e .
   ```

## Dependencies

The following packages will be automatically installed:
- numpy
- matplotlib
- pytest (for running tests)

## Verifying Installation

To verify that the installation was successful, you can run:

```python
from math_art.equations.parametric import ButterflyCurve
import matplotlib.pyplot as plt
import numpy as np

# Create a simple curve
curve = ButterflyCurve(amplitude=2.0)
t = np.linspace(0, 12*np.pi, 1000)
x, y = curve.evaluate(t)

# Plot the curve
plt.figure(figsize=(10, 10))
plt.plot(x, y, c='viridis')
plt.axis('equal')
plt.axis('off')
plt.show()
```

## Troubleshooting

### Common Issues

1. **ImportError: No module named 'math_art'**
   - Make sure you've installed the package correctly
   - Try running `pip install -e .` again
   - Check your Python path

2. **Matplotlib backend issues**
   - If you're using a headless environment, set the backend:
     ```python
     import matplotlib
     matplotlib.use('Agg')
     ```

3. **Memory issues with large fractals**
   - Reduce the resolution or number of iterations
   - Use a smaller range for the fractal

### Getting Help

If you encounter any issues:
1. Check the [FAQ](../docs/faq.md)
2. Open an issue on GitHub
3. Join our community discussions

## Next Steps

- Check out the [Getting Started](../tutorials/getting_started.md) tutorial
- Explore the [Gallery](../gallery.md) for inspiration
- Read the [API Reference](../api/api_reference.md) for detailed documentation 