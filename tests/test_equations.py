import numpy as np
import matplotlib.pyplot as plt
from src.equations import (
    Circle,
    Spiral,
    RoseCurve,
    HeartCurve,
    LissajousCurve,
    MandelbrotSet,
    JuliaSet
)

def test_parametric_equations():
    """Test all parametric equations."""
    # Create instances of each parametric equation
    circle = Circle(radius=2.0)
    spiral = Spiral(growth_rate=1.5)
    rose = RoseCurve(n=5, d=8)
    heart = HeartCurve()
    lissajous = LissajousCurve(a=3, b=2, delta=np.pi/2)
    
    # Generate points for each equation
    circle_x, circle_y = circle.generate_points()
    spiral_x, spiral_y = spiral.generate_points()
    rose_x, rose_y = rose.generate_points()
    heart_x, heart_y = heart.generate_points()
    lissajous_x, lissajous_y = lissajous.generate_points()
    
    # Verify shapes
    assert len(circle_x) == 1000, "Circle points generation failed"
    assert len(spiral_x) == 1000, "Spiral points generation failed"
    assert len(rose_x) == 1000, "Rose curve points generation failed"
    assert len(heart_x) == 1000, "Heart curve points generation failed"
    assert len(lissajous_x) == 1000, "Lissajous curve points generation failed"
    
    print("All parametric equations test passed!")

def test_fractal_equations():
    """Test fractal equations."""
    # Create instances of fractal equations
    mandelbrot = MandelbrotSet(width=800, height=800)
    julia = JuliaSet(width=800, height=800)
    
    # Generate fractal images
    mandelbrot_img = mandelbrot.evaluate(None)
    julia_img = julia.evaluate(None)
    
    # Verify shapes
    assert mandelbrot_img.shape == (800, 800), "Mandelbrot set generation failed"
    assert julia_img.shape == (800, 800), "Julia set generation failed"
    
    print("All fractal equations test passed!")

def test_transformations():
    """Test equation transformations."""
    # Create a circle and apply transformations
    circle = Circle(radius=1.0)
    
    # Test rotation
    x_rot, y_rot = circle.transform(rotation=np.pi/4)
    assert not np.array_equal(x_rot, circle.generate_points()[0]), "Rotation failed"
    
    # Test scaling
    x_scale, y_scale = circle.transform(scale=2.0)
    assert np.max(x_scale) == 2.0, "Scaling failed"
    
    # Test translation
    x_trans, y_trans = circle.transform(translation=(1, 1))
    assert np.min(x_trans) >= 0, "Translation failed"
    
    print("All transformations test passed!")

def visualize_results():
    """Visualize the results of all equations."""
    # Set up the figure
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('Equation Test Results', fontsize=16)
    
    # Create and plot equations
    circle = Circle(radius=2.0)
    spiral = Spiral(growth_rate=1.5)
    rose = RoseCurve(n=5, d=8)
    heart = HeartCurve()
    lissajous = LissajousCurve(a=3, b=2, delta=np.pi/2)
    mandelbrot = MandelbrotSet(width=400, height=400)
    
    # Plot parametric equations
    x, y = circle.generate_points()
    ax1.plot(x, y)
    ax1.set_title('Circle')
    ax1.axis('equal')
    
    x, y = spiral.generate_points()
    ax2.plot(x, y)
    ax2.set_title('Spiral')
    ax2.axis('equal')
    
    x, y = rose.generate_points()
    ax3.plot(x, y)
    ax3.set_title('Rose Curve')
    ax3.axis('equal')
    
    x, y = heart.generate_points()
    ax4.plot(x, y)
    ax4.set_title('Heart Curve')
    ax4.axis('equal')
    
    x, y = lissajous.generate_points()
    ax5.plot(x, y)
    ax5.set_title('Lissajous Curve')
    ax5.axis('equal')
    
    # Plot fractal
    mandelbrot_img = mandelbrot.evaluate(None)
    ax6.imshow(mandelbrot_img, cmap='hot')
    ax6.set_title('Mandelbrot Set')
    ax6.axis('off')
    
    plt.tight_layout()
    plt.savefig('test_results.png')
    plt.close()

if __name__ == "__main__":
    print("Running equation tests...")
    test_parametric_equations()
    test_fractal_equations()
    test_transformations()
    print("Generating visualization...")
    visualize_results()
    print("All tests completed successfully!") 