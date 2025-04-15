# Parametric Equations Theory

This document explains the mathematical theory behind parametric equations used in the Math Art library.

## Introduction to Parametric Equations

Parametric equations define a set of quantities as functions of one or more independent variables called parameters. In our case, we use a single parameter t to define both x and y coordinates:

```python
x = f(t)
y = g(t)
```

where t is the parameter, and f and g are functions that define the curve.

## Common Parametric Curves

### Butterfly Curve

The butterfly curve is defined by:

```python
x = sin(t) * (exp(cos(t)) - 2cos(4t) - sin(t/12)^5)
y = cos(t) * (exp(cos(t)) - 2cos(4t) - sin(t/12)^5)
```

This curve creates a butterfly-like shape with intricate details. The exponential and trigonometric functions combine to create the characteristic wings and patterns.

### Rose Curve (Rhodonea)

The rose curve is defined by:

```python
r = cos(k*t)
x = r * cos(t)
y = r * sin(t)
```

where k is the number of petals. When k is a rational number p/q, the curve has:
- p petals if p and q are both odd
- 2p petals if p is odd and q is even
- p petals if p is even and q is odd

### Lissajous Curve

Lissajous curves are defined by:

```python
x = A * sin(a*t + δ)
y = B * sin(b*t)
```

where:
- A and B are amplitudes
- a and b are frequencies
- δ is the phase difference

These curves are particularly interesting when a/b is a rational number, creating closed curves with various patterns.

## Mathematical Properties

### Periodicity

Many parametric curves are periodic, meaning they repeat their pattern after a certain interval. For example:
- The butterfly curve has a period of 24π
- The rose curve has a period of 2π
- Lissajous curves have a period of 2π * LCM(1/a, 1/b)

### Symmetry

Parametric curves often exhibit various types of symmetry:
- Reflection symmetry across axes
- Rotational symmetry
- Scaling symmetry

### Derivatives and Tangents

The derivative of a parametric curve gives the tangent vector:

```python
dx/dt = f'(t)
dy/dt = g'(t)
```

This is useful for:
- Determining curve direction
- Calculating arc length
- Finding critical points

## Visualization Techniques

### Color Mapping

We can map the parameter t to colors using various schemes:
- Linear mapping: color = t / t_max
- Cyclic mapping: color = (t % period) / period
- Custom functions: color = f(t)

### Line Width

Line width can be varied to create depth:
- Constant width: uniform appearance
- Variable width: creates 3D-like effects
- Width = f(t): can emphasize certain parts of the curve

### Multiple Curves

Combining multiple parametric curves can create complex patterns:
- Superposition: adding coordinates
- Multiplication: multiplying coordinates
- Composition: using one curve's output as another's input

## Applications in Art

Parametric equations are particularly useful for creating mathematical art because:
1. They can create complex, beautiful patterns
2. They are easily parameterized for variation
3. They can be combined to create new forms
4. They often exhibit natural-looking symmetry

## Further Reading

1. [Parametric Equations on Wikipedia](https://en.wikipedia.org/wiki/Parametric_equation)
2. [Beautiful Curves](https://www.mathcurve.com/courbes2d.gb/beautiful/beautiful.shtml)
3. [The Art of Mathematics](https://www.artofmathematics.org/) 