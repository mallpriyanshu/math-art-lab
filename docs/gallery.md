# Math Art Gallery

This gallery showcases various mathematical art pieces created using the Math Art library. Each piece demonstrates different aspects of mathematical beauty through curves, patterns, and fractals.

## Parametric Curves

### Butterfly Curve
![Butterfly Curve](../../images/butterfly.png)
A beautiful butterfly curve created using parametric equations. The gradient colors follow the curve's path, creating a vibrant and dynamic effect. The curve is defined by:
```python
x = sin(t) * (exp(cos(t)) - 2cos(4t) - sin(t/12)^5)
y = cos(t) * (exp(cos(t)) - 2cos(4t) - sin(t/12)^5)
```

### Rose Curve (Rhodonea)
![Rose Curve](../../images/rose.png)
A 7/8 petaled rose curve with elegant pastel pink coloring. The curve demonstrates the beauty of mathematical symmetry. The curve is defined by:
```python
r = cos(7t/8)
x = r * cos(t)
y = r * sin(t)
```

### Lissajous Curve
![Lissajous Curve](../../images/lissajous.png)
A complex Lissajous figure with plasma gradient coloring. These curves show the relationship between two perpendicular oscillations. Parameters: a=5, b=4, δ=π/3
```python
x = sin(5t + π/3)
y = sin(4t)
```

### Spiral
![Spiral](../../images/spiral.png)
A golden spiral with warm salmon coloring. The growth rate is carefully chosen to create an aesthetically pleasing curve.
```python
r = 0.1t
x = r * cos(t)
y = r * sin(t)
```

### Heart Curve
![Heart Curve](../../images/heart.png)
A heart-shaped curve with romantic pink coloring and subtle fill. The curve uses a combination of trigonometric functions to create the heart shape.
```python
x = 16sin³(t)
y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
```

### Trefoil Knot
![Trefoil Knot](../../images/trefoil.png)
A trefoil knot with a gradient from royal blue to light blue. This curve demonstrates the beauty of mathematical knots.
```python
x = sin(t) + 2sin(2t)
y = cos(t) - 2cos(2t)
```

## Fractals

### Mandelbrot Set
![Mandelbrot Set](../../images/mandelbrot.png)
The famous Mandelbrot set rendered with a magma color scheme. This fractal is one of the most well-known mathematical structures, showing incredible complexity from a simple equation:
```python
z_{n+1} = z_n² + c
```

### Julia Set
![Julia Set](../../images/julia.png)
A Julia set with parameter c = -0.7 + 0.27i, rendered with the viridis color scheme. Julia sets are related to the Mandelbrot set and show fascinating patterns based on complex number dynamics.

## Creating Your Own Art

You can create these and many other mathematical art pieces using our library. Here's a quick example:

```python
from math_art.equations.parametric import ButterflyCurve
import matplotlib.pyplot as plt
import numpy as np

curve = ButterflyCurve(amplitude=2.0)
t = np.linspace(0, 12*np.pi, 10000)
x, y = curve.evaluate(t)

plt.figure(figsize=(10, 10))
plt.plot(x, y, c='viridis')
plt.axis('equal')
plt.axis('off')
plt.savefig('my_butterfly.png', dpi=300)
```

Check out our [examples directory](../../examples) for more detailed examples and code to create your own mathematical art! 