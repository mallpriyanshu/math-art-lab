# Directory Structure

This document provides an overview of the Math Art project's directory structure and organization.

## Overview

```
math-art/
├── docs/               # Documentation files
├── examples/           # Example scripts
├── images/            # Generated images
├── src/               # Source code
├── tests/             # Test files
└── [root files]       # Project configuration files
```

## Directory Details

### `docs/` - Documentation
Contains all project documentation, including:
- User guides
- API reference
- Development guides
- Gallery of examples
- Installation instructions
- Contributing guidelines

### `examples/` - Example Scripts
Contains example scripts demonstrating how to use the library:
- `beautiful_math_art.py`: Generates various mathematical art with aesthetic color schemes
- Each example is thoroughly documented and can be run independently
- Examples showcase different features of the library

### `images/` - Generated Images
Stores all generated mathematical art images:
- Parametric curves (butterfly, rose, lissajous, etc.)
- Fractals (Mandelbrot set, Julia set)
- Showcase images for documentation
- Test result visualizations

### `src/` - Source Code
The main source code of the library:
```
src/
├── equations/
│   ├── __init__.py
│   ├── base.py           # Base classes and abstractions
│   ├── parametric.py     # Parametric equation implementations
│   └── fractals.py       # Fractal implementations
└── math_art/
    └── [core modules]    # Core functionality modules
```

### `tests/` - Test Files
Contains all test-related files:
- Unit tests
- Integration tests
- Test utilities
- Test result images
- Coverage reports

### Root Directory Files
Important files in the root directory:
- `setup.py`: Package installation and dependencies
- `requirements.txt`: Project dependencies
- `README.md`: Project overview and quick start
- `CHANGELOG.md`: Version history and changes
- `.gitignore`: Git ignore patterns
- Other configuration files

## File Organization Guidelines

When contributing to the project, please follow these guidelines:

1. **Source Code**
   - Place all source code under `src/`
   - Use appropriate subdirectories for different types of equations
   - Keep the code structure modular and organized

2. **Documentation**
   - Add new documentation files under `docs/`
   - Use clear, descriptive filenames
   - Include examples and usage instructions

3. **Examples**
   - Place example scripts in `examples/`
   - Each example should be self-contained
   - Include comments explaining the code

4. **Tests**
   - Add tests under `tests/`
   - Follow the existing test file naming convention
   - Include both positive and negative test cases

5. **Images**
   - Save generated images in `images/`
   - Use descriptive filenames
   - Include metadata in image generation scripts

## Best Practices

1. **Code Organization**
   - Keep related files together
   - Use consistent naming conventions
   - Maintain clear separation of concerns

2. **Documentation**
   - Keep documentation up-to-date
   - Document all public APIs
   - Include examples in documentation

3. **Testing**
   - Write tests for new features
   - Maintain high test coverage
   - Test edge cases and error conditions

4. **Version Control**
   - Make atomic commits
   - Write clear commit messages
   - Follow branching strategy 