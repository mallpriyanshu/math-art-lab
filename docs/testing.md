# Testing Guide

This guide explains how to run and write tests for the Math Art library.

## Running Tests

### Basic Test Execution

Run all tests using pytest:

```bash
python -m pytest tests/
```

### Specific Test Files

Run a specific test file:

```bash
python -m pytest tests/test_equations.py
```

### Test Coverage

Generate a coverage report:

```bash
python -m pytest --cov=math_art tests/
```

## Writing Tests

### Test Structure

Tests are organized in the `tests/` directory:
```
tests/
├── test_equations.py    # Tests for equation classes
├── test_fractals.py     # Tests for fractal implementations
└── test_utils.py        # Tests for utility functions
```

### Example Test

```python
import pytest
import numpy as np
from math_art.equations.parametric import ButterflyCurve

def test_butterfly_curve():
    # Create curve
    curve = ButterflyCurve(amplitude=2.0)
    
    # Test evaluation
    t = np.linspace(0, 2*np.pi, 100)
    x, y = curve.evaluate(t)
    
    # Check output shape
    assert len(x) == len(y) == 100
    
    # Check amplitude
    assert np.max(np.abs(x)) <= 2.0
    assert np.max(np.abs(y)) <= 2.0
```

### Test Categories

1. **Unit Tests**
   - Test individual components
   - Focus on specific functionality
   - Use mock objects when needed

2. **Integration Tests**
   - Test component interactions
   - Verify end-to-end functionality
   - Check real-world usage scenarios

3. **Visual Tests**
   - Verify image generation
   - Check color schemes
   - Validate output quality

## Test Best Practices

### 1. Test Organization

- Group related tests in classes
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern

```python
class TestButterflyCurve:
    def test_amplitude(self):
        # Arrange
        curve = ButterflyCurve(amplitude=2.0)
        
        # Act
        x, y = curve.evaluate(np.array([0]))
        
        # Assert
        assert np.max(np.abs(x)) <= 2.0
```

### 2. Test Data

- Use fixtures for common data
- Generate test data programmatically
- Include edge cases

```python
@pytest.fixture
def test_points():
    return np.linspace(0, 2*np.pi, 100)

def test_curve_with_fixture(test_points):
    curve = ButterflyCurve()
    x, y = curve.evaluate(test_points)
    assert len(x) == len(test_points)
```

### 3. Assertions

- Use specific assertions
- Check both positive and negative cases
- Verify error conditions

```python
def test_invalid_input():
    curve = ButterflyCurve()
    with pytest.raises(ValueError):
        curve.evaluate(None)
```

## Visual Testing

### Image Comparison

```python
def test_image_generation():
    # Generate image
    curve = ButterflyCurve()
    t = np.linspace(0, 12*np.pi, 1000)
    x, y = curve.evaluate(t)
    
    # Create plot
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, c='viridis')
    plt.axis('equal')
    plt.axis('off')
    
    # Save and compare
    plt.savefig('test_output.png')
    assert compare_images('test_output.png', 'reference.png', tol=0.1)
```

### Performance Testing

```python
def test_performance():
    curve = ButterflyCurve()
    t = np.linspace(0, 12*np.pi, 100000)
    
    start_time = time.time()
    x, y = curve.evaluate(t)
    end_time = time.time()
    
    assert end_time - start_time < 1.0  # Should complete in under 1 second
```

## Continuous Integration

Tests are automatically run on:
- Pull requests
- Push to main branch
- Scheduled runs

See `.github/workflows/tests.yml` for CI configuration.

## Next Steps

- Check the [Development Guide](../development.md) for more testing details
- Review the [API Reference](../api/api_reference.md) for testable components
- Explore existing tests in the `tests/` directory 