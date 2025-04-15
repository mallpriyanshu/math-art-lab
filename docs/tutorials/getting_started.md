# Getting Started with Math Art

This tutorial will guide you through creating your first mathematical art piece using the Math Art library.

## Installation

First, install the library using pip:

```bash
pip install math-art
```

## Creating Your First Curve

Let's create a simple butterfly curve:

```python
from math_art.equations.parametric import ButterflyCurve
import matplotlib.pyplot as plt
import numpy as np

# Create the curve
curve = ButterflyCurve(amplitude=2.0)

# Generate points
t = np.linspace(0, 12*np.pi, 10000)
x, y = curve.evaluate(t)

# Plot the curve
plt.figure(figsize=(10, 10))
plt.plot(x, y, c='viridis')
plt.axis('equal')
plt.axis('off')
plt.savefig('my_first_curve.png', dpi=300)
```

## Understanding the Code

1. **Importing the Library**
   - `ButterflyCurve` is imported from the parametric equations module
   - We also import `matplotlib.pyplot` for plotting and `numpy` for numerical operations

2. **Creating the Curve**
   - `ButterflyCurve(amplitude=2.0)` creates a butterfly curve with amplitude 2.0
   - The amplitude parameter controls the size of the curve

3. **Generating Points**
   - `np.linspace(0, 12*np.pi, 10000)` creates 10000 points between 0 and 12π
   - `curve.evaluate(t)` computes the (x, y) coordinates for each point

4. **Plotting**
   - We create a 10x10 figure
   - Plot the curve with a viridis color scheme
   - Set equal aspect ratio and remove axes
   - Save the figure as a high-resolution PNG

## Creating a Rose Curve

Let's try another example with a rose curve:

```python
from math_art.equations.parametric import RoseCurve
import matplotlib.pyplot as plt
import numpy as np

# Create a 7-petaled rose
curve = RoseCurve(petals=7, amplitude=3.0)

# Generate points
t = np.linspace(0, 2*np.pi, 1000)
x, y = curve.evaluate(t)

# Plot with custom colors
plt.figure(figsize=(10, 10))
plt.plot(x, y, c='#FF69B4', linewidth=2)
plt.axis('equal')
plt.axis('off')
plt.savefig('rose_curve.png', dpi=300)
```

## Creating a Fractal

Let's create a Mandelbrot set:

```python
from math_art.equations.fractals import MandelbrotSet
import matplotlib.pyplot as plt
import numpy as np

# Create the fractal
mandelbrot = MandelbrotSet(max_iter=100)

# Generate the grid
x = np.linspace(-2, 1, 1000)
y = np.linspace(-1.5, 1.5, 1000)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# Compute the fractal
for i in range(len(x)):
    for j in range(len(y)):
        Z[j, i] = mandelbrot.compute(X[j, i], Y[j, i])

# Plot with magma colormap
plt.figure(figsize=(10, 10))
plt.imshow(Z, cmap='magma')
plt.axis('off')
plt.savefig('mandelbrot.png', dpi=300)
```

## Next Steps

1. Try different curves from the parametric equations module
2. Experiment with different color schemes
3. Adjust parameters to create unique variations
4. Combine multiple curves in one plot
5. Create animations of evolving curves

Check out the [Gallery](../../gallery.md) for more inspiration and the [API Reference](../../api/api_reference.md) for detailed documentation of all available features. 