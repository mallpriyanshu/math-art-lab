import numpy as np
import matplotlib.pyplot as plt
from src.equations import (
    Circle,
    Spiral,
    RoseCurve,
    HeartCurve,
    LissajousCurve,
    ButterflyCurve,
    TrefoilKnot,
    KochSnowflake,
    SierpinskiTriangle,
    MandelbrotSet,
    JuliaSet
)

def create_parametric_showcase():
    """Create a showcase of parametric equations."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Parametric Equations Showcase', fontsize=16)
    
    # Rose Curve
    rose = RoseCurve(n=5, d=8, t_range=(0, 2*np.pi), num_points=1000)
    x, y = rose.generate_points()
    ax1.plot(x, y, color='purple')
    ax1.set_title('Rose Curve (n=5, d=8)')
    ax1.axis('equal')
    ax1.axis('off')
    
    # Butterfly Curve
    butterfly = ButterflyCurve(amplitude=2.0, t_range=(0, 12*np.pi), num_points=2000)
    x, y = butterfly.generate_points()
    ax2.plot(x, y, color='blue')
    ax2.set_title('Butterfly Curve')
    ax2.axis('equal')
    ax2.axis('off')
    
    # Heart Curve
    heart = HeartCurve(t_range=(0, 2*np.pi), num_points=1000)
    x, y = heart.generate_points()
    ax3.plot(x, y, color='red')
    ax3.set_title('Heart Curve')
    ax3.axis('equal')
    ax3.axis('off')
    
    # Trefoil Knot
    knot = TrefoilKnot(radius=2.0, t_range=(0, 2*np.pi), num_points=1000)
    x, y = knot.generate_points()
    ax4.plot(x, y, color='green')
    ax4.set_title('Trefoil Knot')
    ax4.axis('equal')
    ax4.axis('off')
    
    plt.tight_layout()
    plt.savefig('showcase_parametric.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_fractal_showcase():
    """Create a showcase of fractal equations."""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Fractal Equations Showcase', fontsize=16)
    
    # Mandelbrot Set
    mandelbrot = MandelbrotSet(width=400, height=400, max_iter=100)
    fractal = mandelbrot.evaluate(None)
    ax1.imshow(fractal, cmap='hot')
    ax1.set_title('Mandelbrot Set')
    ax1.axis('off')
    
    # Julia Set
    julia = JuliaSet(width=400, height=400, c=-0.7 + 0.27j, max_iter=100)
    fractal = julia.evaluate(None)
    ax2.imshow(fractal, cmap='viridis')
    ax2.set_title('Julia Set')
    ax2.axis('off')
    
    # Koch Snowflake
    snowflake = KochSnowflake(iterations=4, size=2.0)
    x, y = snowflake.generate_points()
    ax3.plot(x, y, color='cyan')
    ax3.set_title('Koch Snowflake')
    ax3.axis('equal')
    ax3.axis('off')
    
    # Sierpinski Triangle
    triangle = SierpinskiTriangle(iterations=5, size=2.0)
    x, y = triangle.generate_points()
    ax4.plot(x, y, color='magenta')
    ax4.set_title('Sierpinski Triangle')
    ax4.axis('equal')
    ax4.axis('off')
    
    plt.tight_layout()
    plt.savefig('showcase_fractal.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_combined_showcase():
    """Create a combined showcase of all equations."""
    fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('Math Art Lab Showcase', fontsize=20)
    
    # Rose Curve
    rose = RoseCurve(n=5, d=8, t_range=(0, 2*np.pi), num_points=1000)
    x, y = rose.generate_points()
    ax1.plot(x, y, color='purple')
    ax1.set_title('Rose Curve')
    ax1.axis('equal')
    ax1.axis('off')
    
    # Butterfly Curve
    butterfly = ButterflyCurve(amplitude=2.0, t_range=(0, 12*np.pi), num_points=2000)
    x, y = butterfly.generate_points()
    ax2.plot(x, y, color='blue')
    ax2.set_title('Butterfly Curve')
    ax2.axis('equal')
    ax2.axis('off')
    
    # Mandelbrot Set
    mandelbrot = MandelbrotSet(width=400, height=400, max_iter=100)
    fractal = mandelbrot.evaluate(None)
    ax3.imshow(fractal, cmap='hot')
    ax3.set_title('Mandelbrot Set')
    ax3.axis('off')
    
    # Julia Set
    julia = JuliaSet(width=400, height=400, c=-0.7 + 0.27j, max_iter=100)
    fractal = julia.evaluate(None)
    ax4.imshow(fractal, cmap='viridis')
    ax4.set_title('Julia Set')
    ax4.axis('off')
    
    # Koch Snowflake
    snowflake = KochSnowflake(iterations=4, size=2.0)
    x, y = snowflake.generate_points()
    ax5.plot(x, y, color='cyan')
    ax5.set_title('Koch Snowflake')
    ax5.axis('equal')
    ax5.axis('off')
    
    # Sierpinski Triangle
    triangle = SierpinskiTriangle(iterations=5, size=2.0)
    x, y = triangle.generate_points()
    ax6.plot(x, y, color='magenta')
    ax6.set_title('Sierpinski Triangle')
    ax6.axis('equal')
    ax6.axis('off')
    
    plt.tight_layout()
    plt.savefig('showcase_combined.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    print("Generating showcase images...")
    create_parametric_showcase()
    print("Generated parametric showcase")
    create_fractal_showcase()
    print("Generated fractal showcase")
    create_combined_showcase()
    print("Generated combined showcase")
    print("All showcase images have been generated!") 