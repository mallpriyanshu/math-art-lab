import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import collections as mcoll
from src.equations.parametric import (
    ButterflyCurve,
    RoseCurve,
    LissajousCurve,
    Spiral,
    HeartCurve,
    TrefoilKnot
)
from src.equations.fractals import (
    MandelbrotSet,
    JuliaSet
)

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

def save_figure(name):
    """Helper function to save figures in the images directory."""
    plt.savefig(os.path.join('images', name), dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()

def create_butterfly():
    """Create a beautiful butterfly curve with gradient colors."""
    curve = ButterflyCurve(amplitude=2.0)
    t = np.linspace(0, 12 * np.pi, 10000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    norm = plt.Normalize(t.min(), t.max())
    lc = mcoll.LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(t)
    lc.set_linewidth(2)
    
    plt.gca().add_collection(lc)
    plt.axis('equal')
    plt.axis('off')
    save_figure('butterfly.png')

def create_rose():
    """Create a rose curve with pastel colors."""
    curve = RoseCurve(n=7, d=8)  # 7/8 petaled rose
    t = np.linspace(0, 8 * np.pi, 1000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, c='#FF6B6B', linewidth=3)
    plt.fill(x, y, alpha=0.3, color='#FFE3E3')
    plt.axis('equal')
    plt.axis('off')
    save_figure('rose.png')

def create_lissajous():
    """Create a complex Lissajous figure with gradient colors."""
    curve = LissajousCurve(a=5, b=4, delta=np.pi/3)
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    norm = plt.Normalize(t.min(), t.max())
    lc = mcoll.LineCollection(segments, cmap='plasma', norm=norm)
    lc.set_array(t)
    lc.set_linewidth(2)
    
    plt.gca().add_collection(lc)
    plt.axis('equal')
    plt.axis('off')
    save_figure('lissajous.png')

def create_spiral():
    """Create a golden spiral with warm colors."""
    curve = Spiral(growth_rate=0.1)
    t = np.linspace(0, 8 * np.pi, 1000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, c='#FFA07A', linewidth=3)
    plt.axis('equal')
    plt.axis('off')
    save_figure('spiral.png')

def create_heart():
    """Create a heart curve with romantic colors."""
    curve = HeartCurve()
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    plt.plot(x, y, c='#FF1493', linewidth=3)
    plt.fill(x, y, alpha=0.3, color='#FFB6C1')
    plt.axis('equal')
    plt.axis('off')
    save_figure('heart.png')

def create_trefoil():
    """Create a trefoil knot with cool colors."""
    curve = TrefoilKnot(radius=2.0)
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = curve.evaluate(t)
    
    plt.figure(figsize=(10, 10))
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    
    # Create a custom colormap from royal blue to light blue
    colors = ['#4169E1', '#87CEEB']
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('custom_blues', colors, N=n_bins)
    
    norm = plt.Normalize(t.min(), t.max())
    lc = mcoll.LineCollection(segments, cmap=cmap, norm=norm)
    lc.set_array(t)
    lc.set_linewidth(3)
    
    plt.gca().add_collection(lc)
    plt.axis('equal')
    plt.axis('off')
    save_figure('trefoil.png')

def create_mandelbrot():
    """Create a beautiful Mandelbrot set with custom color scheme."""
    fractal = MandelbrotSet(width=1000, height=1000, max_iter=100)
    result = fractal.evaluate(None)  # t parameter not used for fractals
    
    plt.figure(figsize=(10, 10))
    plt.imshow(result, cmap='magma', extent=[-2, 1, -1.5, 1.5])
    plt.axis('off')
    save_figure('mandelbrot.png')

def create_julia():
    """Create a Julia set with cool colors."""
    fractal = JuliaSet(width=1000, height=1000, c=complex(-0.7, 0.27), max_iter=100)
    result = fractal.evaluate(None)  # t parameter not used for fractals
    
    plt.figure(figsize=(10, 10))
    plt.imshow(result, cmap='viridis', extent=[-2, 2, -2, 2])
    plt.axis('off')
    save_figure('julia.png')

if __name__ == "__main__":
    # Create all the beautiful math art
    create_butterfly()
    create_rose()
    create_lissajous()
    create_spiral()
    create_heart()
    create_trefoil()
    create_mandelbrot()
    create_julia() 