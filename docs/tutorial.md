# Tutorial: Creating Mathematical Art

This tutorial will guide you through creating various types of mathematical art using the math-art package.

## Installation

First, install the package:
```bash
pip install -e .
```

## Basic Usage

### 1. Creating Simple Shapes

Let's start with creating a circle:

```python
import numpy as np
import matplotlib.pyplot as plt
from src.equations import Circle

# Create a circle
circle = Circle(radius=2.0)

# Generate points
x, y = circle.generate_points()

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.axis('equal')
plt.title('Circle')
plt.show()
```

### 2. Creating Complex Patterns

Let's create a rose curve with custom parameters:

```python
from src.equations import RoseCurve

# Create a rose curve with 7 petals
rose = RoseCurve(n=7, d=8)

# Generate points
x, y = rose.generate_points()

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.axis('equal')
plt.title('Rose Curve')
plt.show()
```

### 3. Applying Transformations

Let's create a spiral and apply various transformations:

```python
from src.equations import Spiral

# Create a spiral
spiral = Spiral(growth_rate=1.5)

# Apply transformations
x, y = spiral.transform(
    scale=2.0,
    rotation=np.pi/4,
    translation=(1, 1)
)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x, y)
plt.axis('equal')
plt.title('Transformed Spiral')
plt.show()
```

### 4. Creating Fractals

Let's generate a Mandelbrot set:

```python
from src.equations import MandelbrotSet

# Create a Mandelbrot set
mandelbrot = MandelbrotSet(width=800, height=800, max_iter=100)

# Generate the fractal
fractal = mandelbrot.evaluate(None)

# Plot
plt.figure(figsize=(8, 8))
plt.imshow(fractal, cmap='hot')
plt.axis('off')
plt.title('Mandelbrot Set')
plt.show()
```

### 5. Creating Complex Curves

Let's create a butterfly curve and a trefoil knot:

```python
from src.equations import ButterflyCurve, TrefoilKnot

# Create a butterfly curve
butterfly = ButterflyCurve(amplitude=2.0, t_range=(0, 12*np.pi), num_points=2000)
x, y = butterfly.generate_points()

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='purple')
plt.axis('equal')
plt.title('Butterfly Curve')
plt.show()

# Create a trefoil knot
knot = TrefoilKnot(radius=2.0, t_range=(0, 2*np.pi), num_points=1000)
x, y = knot.generate_points()

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='blue')
plt.axis('equal')
plt.title('Trefoil Knot')
plt.show()
```

### 6. Creating Fractal Patterns

Let's create a Koch snowflake and a Sierpinski triangle:

```python
from src.equations import KochSnowflake, SierpinskiTriangle

# Create a Koch snowflake
snowflake = KochSnowflake(iterations=4, size=2.0)
x, y = snowflake.generate_points()

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='cyan')
plt.axis('equal')
plt.title('Koch Snowflake')
plt.show()

# Create a Sierpinski triangle
triangle = SierpinskiTriangle(iterations=5, size=2.0)
x, y = triangle.generate_points()

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='green')
plt.axis('equal')
plt.title('Sierpinski Triangle')
plt.show()
```

## Advanced Examples

### 1. Creating a Gallery

Let's create a gallery of different mathematical art:

```python
import numpy as np
import matplotlib.pyplot as plt
from src.equations import (
    Circle,
    Spiral,
    RoseCurve,
    HeartCurve,
    LissajousCurve,
    MandelbrotSet
)

# Set up the figure
fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(15, 15))
fig.suptitle('Mathematical Art Gallery', fontsize=16)

# Create and plot equations
circle = Circle(radius=2.0)
spiral = Spiral(growth_rate=1.5)
rose = RoseCurve(n=5, d=8)
heart = HeartCurve()
lissajous = LissajousCurve(a=3, b=2, delta=np.pi/2)
mandelbrot = MandelbrotSet(width=400, height=400)

# Plot each equation
x, y = circle.generate_points()
ax1.plot(x, y)
ax1.set_title('Circle')
ax1.axis('equal')

x, y = spiral.generate_points()
ax2.plot(x, y)
ax2.set_title('Spiral')
ax2.axis('equal')

x, y = rose.generate_points()
ax3.plot(x, y)
ax3.set_title('Rose Curve')
ax3.axis('equal')

x, y = heart.generate_points()
ax4.plot(x, y)
ax4.set_title('Heart Curve')
ax4.axis('equal')

x, y = lissajous.generate_points()
ax5.plot(x, y)
ax5.set_title('Lissajous Curve')
ax5.axis('equal')

mandelbrot_img = mandelbrot.evaluate(None)
ax6.imshow(mandelbrot_img, cmap='hot')
ax6.set_title('Mandelbrot Set')
ax6.axis('off')

plt.tight_layout()
plt.show()
```

### 2. Creating Custom Equations

Let's create a custom equation for a butterfly curve:

```python
from src.equations import MathEquation

class ButterflyCurve(MathEquation):
    def evaluate(self, t):
        x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
        y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
        return x, y

# Create and plot the butterfly curve
butterfly = ButterflyCurve(t_range=(0, 12*np.pi), num_points=2000)
x, y = butterfly.generate_points()

plt.figure(figsize=(8, 8))
plt.plot(x, y, color='purple')
plt.axis('equal')
plt.title('Butterfly Curve')
plt.show()
```

## Tips and Tricks

1. **Parameter Tuning**
   - Experiment with different parameters to create unique patterns
   - For fractals, try different max_iter values to control detail level
   - For parametric curves, adjust the t_range for different curve lengths

2. **Visualization**
   - Use different colormaps for fractals
   - Adjust line widths and colors for parametric curves
   - Try different figure sizes for optimal viewing

3. **Performance**
   - For high-resolution fractals, increase max_iter gradually
   - For complex parametric curves, adjust num_points as needed
   - Use appropriate t_range to avoid unnecessary computations

4. **Customization**
   - Combine multiple equations for complex patterns
   - Apply transformations to create variations
   - Create your own equation classes for unique art 