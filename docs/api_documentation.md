# API Documentation

## Base Equation Class

### `MathEquation`
Base class for all mathematical equations.

#### Parameters
- `t_range` (tuple): Range of parameter t (default: (0, 2π))
- `num_points` (int): Number of points to generate (default: 1000)

#### Methods
- `evaluate(t)`: Abstract method to evaluate the equation at parameter t
- `generate_points()`: Generate points for the entire parameter range
- `transform(scale=1.0, rotation=0.0, translation=(0, 0))`: Apply transformations to the equation

## Parametric Equations

### `Circle`
Parametric equation for a circle.

#### Parameters
- `radius` (float): Radius of the circle (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
x = radius * cos(t)
y = radius * sin(t)
```

### `Spiral`
Parametric equation for a spiral.

#### Parameters
- `growth_rate` (float): Rate at which the spiral grows (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
r = growth_rate * t
x = r * cos(t)
y = r * sin(t)
```

### `RoseCurve`
Parametric equation for a rose curve (rhodonea curve).

#### Parameters
- `n` (int): Number of petals (default: 5)
- `d` (int): Denominator affecting petal shape (default: 8)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
r = cos(n/d * t)
x = r * cos(t)
y = r * sin(t)
```

### `HeartCurve`
Parametric equation for a heart-shaped curve.

#### Parameters
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
x = 16 * sin³(t)
y = 13 * cos(t) - 5 * cos(2t) - 2 * cos(3t) - cos(4t)
```

### `LissajousCurve`
Parametric equation for a Lissajous curve.

#### Parameters
- `a` (float): Frequency in x-direction (default: 3)
- `b` (float): Frequency in y-direction (default: 2)
- `delta` (float): Phase difference (default: π/2)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
x = sin(a * t + delta)
y = sin(b * t)
```

### `ButterflyCurve`
Parametric equation for a butterfly-shaped curve.

#### Parameters
- `amplitude` (float): Amplitude of the curve (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
x = amplitude * sin(t) * (exp(cos(t)) - 2 * cos(4t) - sin(t/12)^5)
y = amplitude * cos(t) * (exp(cos(t)) - 2 * cos(4t) - sin(t/12)^5)
```

### `TrefoilKnot`
Parametric equation for a trefoil knot.

#### Parameters
- `radius` (float): Radius of the knot (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
x = radius * (sin(t) + 2 * sin(2t))
y = radius * (cos(t) - 2 * cos(2t))
```

## Fractal Equations

### `MandelbrotSet`
Implementation of the Mandelbrot set.

#### Parameters
- `width` (int): Width of the output image (default: 800)
- `height` (int): Height of the output image (default: 800)
- `max_iter` (int): Maximum number of iterations (default: 100)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
zₙ₊₁ = zₙ² + c
```

### `JuliaSet`
Implementation of the Julia set.

#### Parameters
- `width` (int): Width of the output image (default: 800)
- `height` (int): Height of the output image (default: 800)
- `c` (complex): Complex constant (default: -0.7 + 0.27j)
- `max_iter` (int): Maximum number of iterations (default: 100)
- `**kwargs`: Additional parameters passed to MathEquation

#### Equation
```
zₙ₊₁ = zₙ² + c
```

### `KochSnowflake`
Implementation of the Koch snowflake fractal.

#### Parameters
- `iterations` (int): Number of iterations (default: 4)
- `size` (float): Size of the snowflake (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Description
The Koch snowflake is constructed by recursively replacing each line segment with four shorter segments, forming an equilateral triangle in the middle third.

### `SierpinskiTriangle`
Implementation of the Sierpinski triangle fractal.

#### Parameters
- `iterations` (int): Number of iterations (default: 5)
- `size` (float): Size of the triangle (default: 1.0)
- `**kwargs`: Additional parameters passed to MathEquation

#### Description
The Sierpinski triangle is constructed by recursively subdividing an equilateral triangle into smaller equilateral triangles.

## Usage Examples

### Creating a Circle
```python
from src.equations import Circle

# Create a circle with radius 2.0
circle = Circle(radius=2.0)

# Generate points
x, y = circle.generate_points()

# Apply transformations
x_transformed, y_transformed = circle.transform(
    scale=1.5,
    rotation=np.pi/4,
    translation=(1, 1)
)
```

### Creating a Mandelbrot Set
```python
from src.equations import MandelbrotSet

# Create a Mandelbrot set
mandelbrot = MandelbrotSet(width=800, height=800, max_iter=100)

# Generate the fractal
fractal = mandelbrot.evaluate(None)
```

### Creating a Custom Equation
```python
from src.equations import MathEquation

class CustomCurve(MathEquation):
    def __init__(self, amplitude=1.0, frequency=1.0, **kwargs):
        super().__init__(**kwargs)
        self.amplitude = amplitude
        self.frequency = frequency
    
    def evaluate(self, t):
        x = self.amplitude * np.sin(self.frequency * t)
        y = self.amplitude * np.cos(self.frequency * t)
        return x, y
``` 