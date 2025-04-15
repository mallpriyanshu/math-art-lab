# Mathematical Art Generator

A Python project for generating beautiful mathematical art using various mathematical concepts and equations. This project demonstrates the intersection of mathematics and art through code, with a focus on clean, extensible, and well-organized implementation.

## Project Structure

```
math-art/
├── src/
│   ├── equations/           # Mathematical equation implementations
│   │   ├── __init__.py     # Package initialization and exports
│   │   ├── base.py         # Base equation class and common functionality
│   │   ├── parametric.py   # Parametric equations (circles, spirals, etc.)
│   │   └── fractals.py     # Fractal equations (Mandelbrot, Julia sets)
│   └── math_art/           # Main application and visualization code
│       └── math_art.py     # Main application entry point
├── examples/               # Example scripts
│   ├── math-draw.py       # Basic drawing examples
│   └── custom_art.py      # Custom art generation examples
├── docs/                  # Documentation
│   └── mathematical_equations.md  # Detailed equation documentation
└── requirements.txt       # Project dependencies
```

## Mathematical Concepts

### Equation Organization
The project uses an object-oriented approach to organize mathematical equations:

1. **Base Equation Class**
   - Provides common functionality for all equations
   - Handles transformations (scale, rotate, translate)
   - Manages parameter ranges and point generation

2. **Parametric Equations**
   - Circle: `x = r * cos(θ), y = r * sin(θ)`
   - Spiral: `x = a * θ * cos(θ), y = a * θ * sin(θ)`
   - Rose Curve: `r = cos(n/d * θ), x = r * cos(θ), y = r * sin(θ)`
   - Heart Curve: `x = 16 * sin³(θ), y = 13 * cos(θ) - 5 * cos(2θ) - 2 * cos(3θ) - cos(4θ)`
   - Lissajous Curve: `x = sin(a * θ + δ), y = sin(b * θ)`

3. **Fractal Equations**
   - Mandelbrot Set: `zₙ₊₁ = zₙ² + c`
   - Julia Set: `zₙ₊₁ = zₙ² + c` (with fixed c)

### Transformation Equations
All equations support the following transformations:
- Rotation: `x' = x * cos(θ) - y * sin(θ), y' = x * sin(θ) + y * cos(θ)`
- Scaling: `x' = s * x, y' = s * y`
- Translation: `x' = x + t_x, y' = y + t_y`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/math-art.git
cd math-art
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running Examples
```bash
# Run the main gallery
python src/math_art/math_art.py

# Run custom examples
python examples/custom_art.py
```

### Creating Custom Art
1. Import the required equation classes:
```python
from src.equations import Circle, Spiral, RoseCurve
```

2. Create and customize equations:
```python
# Create a circle
circle = Circle(radius=2.0)

# Create a spiral with custom parameters
spiral = Spiral(growth_rate=1.5, t_range=(0, 4*np.pi))

# Apply transformations
x, y = spiral.transform(scale=2.0, rotation=np.pi/4, translation=(1, 1))
```

3. Visualize the results:
```python
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()
```

## Extending the Project

To add new mathematical art:

1. Choose the appropriate category (parametric or fractal)
2. Create a new class inheriting from `MathEquation`:
```python
from src.equations.base import MathEquation

class NewCurve(MathEquation):
    def __init__(self, param1=1.0, **kwargs):
        super().__init__(**kwargs)
        self.param1 = param1
    
    def evaluate(self, t):
        x = self.param1 * np.sin(t)
        y = self.param1 * np.cos(t)
        return x, y
```

3. Add the class to the appropriate module and `__init__.py`
4. Document the equations and parameters used

## Dependencies
- numpy
- matplotlib
- pillow

## License
MIT License

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request. 