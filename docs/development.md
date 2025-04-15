# Development Guide

This guide provides information for developers who want to contribute to the math-art project.

## Project Structure

```
math-art/
├── src/
│   ├── equations/           # Mathematical equation implementations
│   │   ├── __init__.py     # Package initialization and exports
│   │   ├── base.py         # Base equation class and common functionality
│   │   ├── parametric.py   # Parametric equations
│   │   └── fractals.py     # Fractal equations
│   └── math_art/           # Main application code
├── tests/                  # Test files
├── examples/              # Example scripts
├── docs/                  # Documentation
└── setup.py              # Package configuration
```

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/math-art.git
cd math-art
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -e ".[dev]"
```

## Adding New Equations

### 1. Choose the Appropriate Category

- **Parametric Equations**: For equations that can be expressed as x = f(t), y = g(t)
- **Fractal Equations**: For equations that generate fractal patterns

### 2. Create the Equation Class

For parametric equations:
```python
from .base import MathEquation

class NewEquation(MathEquation):
    def __init__(self, param1=1.0, param2=1.0, **kwargs):
        super().__init__(**kwargs)
        self.param1 = param1
        self.param2 = param2
    
    def evaluate(self, t):
        x = self.param1 * np.sin(self.param2 * t)
        y = self.param1 * np.cos(self.param2 * t)
        return x, y
```

For fractal equations:
```python
from .base import MathEquation

class NewFractal(MathEquation):
    def __init__(self, width=800, height=800, max_iter=100, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.max_iter = max_iter
    
    def evaluate(self, t):
        # Implementation of fractal generation
        pass
```

### 3. Add Tests

Create a test file in the `tests` directory:
```python
def test_new_equation():
    equation = NewEquation(param1=2.0, param2=3.0)
    x, y = equation.generate_points()
    assert len(x) == 1000
    assert len(y) == 1000
```

### 4. Update Documentation

1. Add the equation to `docs/api_documentation.md`
2. Add examples to `docs/tutorial.md`
3. Update the README if necessary

## Testing

Run all tests:
```bash
python -m pytest tests/
```

Run specific test file:
```bash
python -m pytest tests/test_equations.py
```

## Code Style

Follow PEP 8 guidelines:
- Use 4 spaces for indentation
- Limit lines to 79 characters
- Use descriptive variable names
- Add docstrings to all classes and methods

Example:
```python
class ExampleEquation(MathEquation):
    """Example equation for demonstration purposes.
    
    This equation generates a pattern based on the given parameters.
    
    Parameters
    ----------
    amplitude : float
        The amplitude of the pattern
    frequency : float
        The frequency of the pattern
    """
    
    def __init__(self, amplitude=1.0, frequency=1.0, **kwargs):
        super().__init__(**kwargs)
        self.amplitude = amplitude
        self.frequency = frequency
```

## Pull Request Process

1. Create a new branch for your feature/fix
2. Make your changes
3. Run tests and ensure they pass
4. Update documentation
5. Submit a pull request

## Release Process

1. Update version in `setup.py`
2. Update CHANGELOG.md
3. Create a new release on GitHub
4. Tag the release
5. Update PyPI package (if applicable)

## Common Issues and Solutions

### 1. Equation Not Rendering Correctly
- Check parameter ranges
- Verify transformation order
- Ensure proper scaling

### 2. Performance Issues
- Optimize number of points
- Use numpy vectorization
- Consider caching results

### 3. Memory Issues
- Reduce resolution for large fractals
- Use generators for large datasets
- Implement chunking for large computations

## Contributing Guidelines

1. **Code Quality**
   - Write clean, well-documented code
   - Follow PEP 8 guidelines
   - Add type hints where appropriate

2. **Testing**
   - Write tests for new features
   - Ensure all tests pass
   - Add test coverage for edge cases

3. **Documentation**
   - Update API documentation
   - Add usage examples
   - Document new parameters

4. **Performance**
   - Optimize for large datasets
   - Use efficient algorithms
   - Consider memory usage

5. **Compatibility**
   - Support Python 3.8+
   - Test on different platforms
   - Handle edge cases gracefully 