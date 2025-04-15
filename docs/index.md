# Math Art Documentation

Welcome to the Math Art documentation! This library allows you to create beautiful mathematical art using Python, combining mathematical equations with aesthetic visualization.

## Quick Links

- [Gallery](gallery.md) - View beautiful mathematical art examples
- [Installation](installation.md) - Get started with the library
- [User Guide](user_guide.md) - Learn how to use the library
- [API Reference](api/api_reference.md) - Detailed API documentation
- [Development Guide](development.md) - Contribute to the project
- [Directory Structure](directory_structure.md) - Project organization

## Overview

Math Art is a Python library that transforms mathematical equations into beautiful visual art. It provides:

- Parametric curves (butterfly, rose, lissajous, etc.)
- Fractals (Mandelbrot set, Julia set)
- Customizable color schemes
- High-quality image generation
- Easy-to-use API

## Getting Started

1. Install the package:
   ```bash
   pip install math-art
   ```

2. Create your first piece of math art:
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

## Documentation Sections

### User Documentation
- [Installation Guide](installation.md) - How to install and set up the library
- [User Guide](user_guide.md) - Comprehensive guide to using the library
- [Examples](examples.md) - Collection of example scripts
- [Gallery](gallery.md) - Showcase of mathematical art

### Developer Documentation
- [Development Guide](development.md) - How to contribute to the project
- [API Reference](api/api_reference.md) - Detailed API documentation
- [Directory Structure](directory_structure.md) - Project organization
- [Testing Guide](testing.md) - How to run and write tests

### Mathematical Background
- [Parametric Equations](theory/parametric_equations.md) - Understanding parametric curves
- [Fractals](theory/fractals.md) - Mathematical theory behind fractals
- [Color Theory](theory/colors.md) - Creating aesthetic color schemes

## Features

### Parametric Curves
- Butterfly curve
- Rose curves
- Lissajous figures
- Spirals
- Heart curves
- Trefoil knots
- And many more...

### Fractals
- Mandelbrot set
- Julia sets
- Customizable parameters
- High-resolution rendering

### Visualization
- Custom color schemes
- Gradient coloring
- High DPI output
- Clean, professional presentation

## Contributing

We welcome contributions! Please see our:
- [Contributing Guidelines](contributing.md)
- [Development Guide](development.md)
- [Code of Conduct](code_of_conduct.md)

## Support

- [GitHub Issues](https://github.com/yourusername/math-art/issues) - Report bugs or request features
- [Discussions](https://github.com/yourusername/math-art/discussions) - Ask questions and share ideas
- [Examples](examples.md) - Learn from example code

## License

This project is licensed under the MIT License - see the [LICENSE](../../LICENSE) file for details.

## Acknowledgments

- [Matplotlib](https://matplotlib.org/) - For visualization
- [NumPy](https://numpy.org/) - For numerical computations
- All our contributors and users 