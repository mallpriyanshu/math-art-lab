# User Guide

This guide provides comprehensive information about using the Math Art library to create beautiful mathematical art.

## Table of Contents

1. [Basic Concepts](#basic-concepts)
2. [Creating Curves](#creating-curves)
3. [Creating Fractals](#creating-fractals)
4. [Customizing Appearance](#customizing-appearance)
5. [Advanced Techniques](#advanced-techniques)
6. [Best Practices](#best-practices)

## Basic Concepts

### Parametric Equations

Parametric equations define curves using a parameter t:
```python
x = f(t)
y = g(t)
```

### Fractals

Fractals are complex patterns that repeat at different scales. The library supports:
- Mandelbrot set
- Julia sets
- Custom fractal implementations

## Creating Curves

### Basic Curve Creation

```python
from math_art.equations.parametric import ButterflyCurve
import matplotlib.pyplot as plt
import numpy as np

# Create the curve
curve = ButterflyCurve(amplitude=2.0)

# Generate points
t = np.linspace(0, 12*np.pi, 10000)
x, y = curve.evaluate(t)

# Plot
plt.figure(figsize=(10, 10))
plt.plot(x, y, c='viridis')
plt.axis('equal')
plt.axis('off')
plt.show()
```

### Available Curves

1. **Butterfly Curve**
   ```python
   curve = ButterflyCurve(amplitude=2.0)
   ```

2. **Rose Curve**
   ```python
   curve = RoseCurve(petals=7, amplitude=3.0)
   ```

3. **Lissajous Curve**
   ```python
   curve = LissajousCurve(a=5, b=4, delta=np.pi/3)
   ```

## Creating Fractals

### Basic Fractal Creation

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

# Plot
plt.figure(figsize=(10, 10))
plt.imshow(Z, cmap='magma')
plt.axis('off')
plt.show()
```

### Available Fractals

1. **Mandelbrot Set**
   ```python
   fractal = MandelbrotSet(max_iter=100)
   ```

2. **Julia Set**
   ```python
   fractal = JuliaSet(c=-0.7 + 0.27j, max_iter=100)
   ```

## Customizing Appearance

### Color Schemes

1. **Built-in Colormaps**
   ```python
   plt.plot(x, y, c='viridis')  # or 'plasma', 'magma', etc.
   ```

2. **Custom Gradients**
   ```python
   from math_art.utils.colors import create_gradient
   colors = create_gradient(['#FF0000', '#00FF00', '#0000FF'])
   ```

### Line Styles

```python
plt.plot(x, y, 
         linewidth=2,    # Line width
         alpha=0.8,      # Transparency
         linestyle='-')  # Line style
```

## Advanced Techniques

### Combining Curves

```python
# Create multiple curves
butterfly = ButterflyCurve(amplitude=2.0)
rose = RoseCurve(petals=7, amplitude=3.0)

# Generate points
t = np.linspace(0, 12*np.pi, 10000)
x1, y1 = butterfly.evaluate(t)
x2, y2 = rose.evaluate(t)

# Plot together
plt.figure(figsize=(10, 10))
plt.plot(x1, y1, c='blue', alpha=0.5)
plt.plot(x2, y2, c='red', alpha=0.5)
plt.axis('equal')
plt.axis('off')
plt.show()
```

### Animations

```python
import matplotlib.animation as animation

fig = plt.figure(figsize=(10, 10))
curve = ButterflyCurve(amplitude=2.0)
t = np.linspace(0, 12*np.pi, 1000)

def update(frame):
    plt.clf()
    x, y = curve.evaluate(t + frame/10)
    plt.plot(x, y, c='viridis')
    plt.axis('equal')
    plt.axis('off')

ani = animation.FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

## Best Practices

1. **Performance**
   - Use appropriate number of points for curves
   - Adjust fractal resolution based on needs
   - Consider using vectorized operations

2. **Visual Quality**
   - Use high DPI for final images
   - Choose appropriate color schemes
   - Consider aspect ratio and scaling

3. **Code Organization**
   - Create reusable functions for common patterns
   - Document your code
   - Use meaningful variable names

## Next Steps

- Explore the [Gallery](../gallery.md) for inspiration
- Check out the [API Reference](../api/api_reference.md) for detailed documentation
- Try the [Tutorials](../tutorials/getting_started.md) for step-by-step guides 