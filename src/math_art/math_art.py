import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from ..equations import (
    MandelbrotSet,
    JuliaSet,
    RoseCurve,
    HeartCurve,
    Spiral,
    LissajousCurve
)

def generate_mandelbrot(width, height, max_iter=100):
    """Generate a Mandelbrot set fractal."""
    x = np.linspace(-2, 1, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def generate_parametric_flower():
    """Generate a parametric flower pattern."""
    t = np.linspace(0, 2*np.pi, 1000)
    r = np.sin(5*t) * np.cos(3*t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

def generate_lissajous_curve(a=3, b=2, delta=np.pi/2):
    """Generate a Lissajous curve."""
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(a*t + delta)
    y = np.sin(b*t)
    return x, y

def create_custom_colormap():
    """Create a custom colormap for the visualizations."""
    colors = ['#000000', '#1a1a2e', '#16213e', '#0f3460', '#533483', '#e94560']
    return LinearSegmentedColormap.from_list('custom', colors)

def generate_julia_set(width, height, c=-0.7 + 0.27j, max_iter=100):
    """Generate a Julia set fractal."""
    x = np.linspace(-2, 2, width)
    y = np.linspace(-2, 2, height)
    X, Y = np.meshgrid(x, y)
    z = X + 1j * Y
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def generate_heart_curve():
    """Generate a heart-shaped curve."""
    t = np.linspace(0, 2*np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

def generate_rose_curve(n=5, d=8):
    """Generate a rose curve (rhodonea curve)."""
    t = np.linspace(0, 2*np.pi, 1000)
    r = np.cos(n/d * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

def generate_spiral():
    """Generate a beautiful spiral pattern."""
    t = np.linspace(0, 8*np.pi, 1000)
    r = t
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

def main():
    # Set up the figure and subplots
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(15, 15))
    fig.suptitle('Mathematical Art Gallery', fontsize=16)
    
    # Generate and plot Mandelbrot set
    mandelbrot = MandelbrotSet(width=800, height=800)
    mandelbrot_img = mandelbrot.evaluate(None)  # t parameter not used for fractals
    ax1.imshow(mandelbrot_img, cmap=create_custom_colormap())
    ax1.set_title('Mandelbrot Set')
    ax1.axis('off')
    
    # Generate and plot Julia set
    julia = JuliaSet(width=800, height=800)
    julia_img = julia.evaluate(None)  # t parameter not used for fractals
    ax2.imshow(julia_img, cmap=create_custom_colormap())
    ax2.set_title('Julia Set')
    ax2.axis('off')
    
    # Generate and plot rose curve
    rose = RoseCurve(n=5, d=8)
    x_rose, y_rose = rose.generate_points()
    ax3.plot(x_rose, y_rose, color='#e94560', linewidth=2)
    ax3.set_title('Rose Curve')
    ax3.axis('equal')
    ax3.axis('off')
    
    # Generate and plot heart curve
    heart = HeartCurve()
    x_heart, y_heart = heart.generate_points()
    ax4.plot(x_heart, y_heart, color='#ff0000', linewidth=2)
    ax4.set_title('Heart Curve')
    ax4.axis('equal')
    ax4.axis('off')
    
    # Generate and plot Lissajous curve
    lissajous = LissajousCurve(a=3, b=2, delta=np.pi/2)
    x_liss, y_liss = lissajous.generate_points()
    ax5.plot(x_liss, y_liss, color='#533483', linewidth=2)
    ax5.set_title('Lissajous Curve')
    ax5.axis('equal')
    ax5.axis('off')
    
    # Generate and plot spiral
    spiral = Spiral(growth_rate=1.0)
    x_spiral, y_spiral = spiral.generate_points()
    ax6.plot(x_spiral, y_spiral, color='#0f3460', linewidth=2)
    ax6.set_title('Spiral')
    ax6.axis('equal')
    ax6.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 