# Math Art Lab

A Python library for creating beautiful mathematical art through parametric equations and fractals.

![Math Art Lab Showcase](showcase_combined.png)

## Features

- **Parametric Equations**
  - Rose Curves: Beautiful flower-like patterns with adjustable petal count
  - Butterfly Curves: Intricate butterfly-shaped patterns
  - Heart Curves: Mathematical heart shapes
  - Trefoil Knots: Three-lobed mathematical knots
  - And more...

- **Fractal Equations**
  - Mandelbrot Set: The famous set of complex numbers with stunning detail
  - Julia Set: A family of beautiful fractals with adjustable parameters
  - Koch Snowflake: A classic fractal with infinite perimeter
  - Sierpinski Triangle: A self-similar triangular pattern

- **Transformations**
  - Rotation: Rotate any curve around its center
  - Scaling: Adjust the size of patterns
  - Translation: Move patterns in any direction

## Installation

```bash
# From PyPI (coming soon)
pip install math-art-lab

# From source
git clone https://github.com/yourusername/math-art-lab.git
cd math-art-lab
pip install -e .
```

## Quick Start

```python
from src.equations import RoseCurve, MandelbrotSet
import matplotlib.pyplot as plt
import numpy as np

# Create a rose curve
rose = RoseCurve(n=5, d=8, t_range=(0, 2*np.pi), num_points=1000)
x, y = rose.generate_points()

# Plot with custom styling
plt.figure(figsize=(8, 8))
plt.plot(x, y, color='purple', linewidth=1.5)
plt.title('Rose Curve (n=5, d=8)')
plt.axis('equal')
plt.axis('off')
plt.show()

# Create a Mandelbrot set
mandelbrot = MandelbrotSet(width=800, height=800, max_iter=100)
fractal = mandelbrot.evaluate(None)

# Plot with custom colormap
plt.figure(figsize=(10, 10))
plt.imshow(fractal, cmap='hot', extent=[-2, 1, -1.5, 1.5])
plt.title('Mandelbrot Set')
plt.axis('off')
plt.show()
```

## Gallery

### Parametric Equations
Beautiful curves generated using parametric equations:
![Parametric Equations Showcase](showcase_parametric.png)

### Fractal Equations
Complex and intricate fractal patterns:
![Fractal Equations Showcase](showcase_fractal.png)

## Documentation

- [API Documentation](docs/api_documentation.md): Detailed documentation of all equations and parameters
- [Tutorial](docs/tutorial.md): Step-by-step guide to creating mathematical art
- [Development Guide](docs/development.md): Guide for contributors

## Examples

The `examples/` directory contains several example scripts:
- `showcase.py`: Generate beautiful showcase images
- `custom_art.py`: Examples of creating custom art
- `math-draw.py`: Interactive drawing examples

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run the tests (`python -m pytest tests/`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

See our [Development Guide](docs/development.md) for detailed contribution guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the beauty of mathematical patterns and equations
- Built with Python, NumPy, and Matplotlib
- Special thanks to all contributors 