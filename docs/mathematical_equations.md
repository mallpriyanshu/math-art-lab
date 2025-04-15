# Mathematical Equations Documentation

This document provides detailed explanations of the mathematical equations used in the project.

## 1. Mandelbrot Set

### Core Equation
```
zₙ₊₁ = zₙ² + c
```

Where:
- zₙ is a complex number at iteration n
- c is a complex constant
- The sequence is bounded if |zₙ| ≤ 2 for all n

### Implementation Details
- The iteration continues until either:
  - |zₙ| > 2 (point is not in the set)
  - Maximum iterations reached (point is likely in the set)
- Color mapping is based on the number of iterations before divergence

## 2. Parametric Equations

### Circle
```
x = r * cos(θ)
y = r * sin(θ)
```
Where:
- r is the radius
- θ is the angle parameter (0 to 2π)

### Spiral
```
x = a * θ * cos(θ)
y = a * θ * sin(θ)
```
Where:
- a is the spiral growth rate
- θ is the angle parameter

## 3. Transformation Equations

### Rotation
```
x' = x * cos(θ) - y * sin(θ)
y' = x * sin(θ) + y * cos(θ)
```
Where:
- (x, y) are original coordinates
- (x', y') are rotated coordinates
- θ is the rotation angle

### Scaling
```
x' = s * x
y' = s * y
```
Where:
- s is the scale factor
- (x, y) are original coordinates
- (x', y') are scaled coordinates

### Translation
```
x' = x + t_x
y' = y + t_y
```
Where:
- (t_x, t_y) is the translation vector
- (x, y) are original coordinates
- (x', y') are translated coordinates

## 4. Color Mapping

### Linear Color Mapping
```
color = (iteration_count / max_iterations) * color_range
```
Where:
- iteration_count is the number of iterations before divergence
- max_iterations is the maximum allowed iterations
- color_range is the range of colors to map to

### Smooth Coloring
```
color = iteration_count + 1 - log(log(|zₙ|)) / log(2)
```
Provides smoother color transitions in the Mandelbrot set visualization.

## 5. Animation Equations

### Zoom Transformation
```
scale = initial_scale * (zoom_factor)^t
```
Where:
- initial_scale is the starting zoom level
- zoom_factor is the rate of zoom
- t is the time parameter

### Pan Transformation
```
x_offset = amplitude * sin(frequency * t)
y_offset = amplitude * cos(frequency * t)
```
Creates smooth panning motion in animations. 