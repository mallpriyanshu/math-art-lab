import numpy as np
from .base import MathEquation

class MandelbrotSet(MathEquation):
    """Implementation of the Mandelbrot set."""
    def __init__(self, width=800, height=800, max_iter=100, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.max_iter = max_iter
    
    def evaluate(self, t):
        # Create complex plane
        x = np.linspace(-2, 1, self.width)
        y = np.linspace(-1.5, 1.5, self.height)
        X, Y = np.meshgrid(x, y)
        c = X + 1j * Y
        
        # Initialize z and divergence time
        z = np.zeros_like(c)
        divtime = self.max_iter + np.zeros(z.shape, dtype=int)
        
        # Iterate
        for i in range(self.max_iter):
            z = z**2 + c
            diverge = z*np.conj(z) > 2**2
            div_now = diverge & (divtime == self.max_iter)
            divtime[div_now] = i
            z[diverge] = 2
        
        return divtime

class JuliaSet(MathEquation):
    """Implementation of the Julia set."""
    def __init__(self, width=800, height=800, c=-0.7 + 0.27j, max_iter=100, **kwargs):
        super().__init__(**kwargs)
        self.width = width
        self.height = height
        self.c = c
        self.max_iter = max_iter
    
    def evaluate(self, t):
        # Create complex plane
        x = np.linspace(-2, 2, self.width)
        y = np.linspace(-2, 2, self.height)
        X, Y = np.meshgrid(x, y)
        z = X + 1j * Y
        
        # Initialize divergence time
        divtime = self.max_iter + np.zeros(z.shape, dtype=int)
        
        # Iterate
        for i in range(self.max_iter):
            z = z**2 + self.c
            diverge = z*np.conj(z) > 2**2
            div_now = diverge & (divtime == self.max_iter)
            divtime[div_now] = i
            z[diverge] = 2
        
        return divtime 

class KochSnowflake(MathEquation):
    """Koch snowflake fractal.
    
    A fractal curve that resembles a snowflake.
    
    Parameters
    ----------
    iterations : int
        Number of iterations (default: 4)
    size : float
        Size of the snowflake (default: 1.0)
    **kwargs : dict
        Additional parameters passed to MathEquation
    """
    
    def __init__(self, iterations=4, size=1.0, **kwargs):
        super().__init__(**kwargs)
        self.iterations = iterations
        self.size = size
    
    def _koch_curve(self, p1, p2, iterations):
        if iterations == 0:
            return [p1, p2]
        
        # Calculate the three points of the equilateral triangle
        p1 = np.array(p1)
        p2 = np.array(p2)
        v = p2 - p1
        p3 = p1 + v/3
        p5 = p1 + 2*v/3
        p4 = p3 + np.array([
            v[0]*np.cos(np.pi/3) - v[1]*np.sin(np.pi/3),
            v[0]*np.sin(np.pi/3) + v[1]*np.cos(np.pi/3)
        ]) / 3
        
        return (self._koch_curve(p1, p3, iterations-1) +
                self._koch_curve(p3, p4, iterations-1) +
                self._koch_curve(p4, p5, iterations-1) +
                self._koch_curve(p5, p2, iterations-1))
    
    def evaluate(self, t):
        # Create initial triangle
        p1 = np.array([0, 0])
        p2 = np.array([self.size, 0])
        p3 = np.array([self.size/2, self.size * np.sqrt(3)/2])
        
        # Generate points for each side
        points = (self._koch_curve(p1, p2, self.iterations) +
                 self._koch_curve(p2, p3, self.iterations) +
                 self._koch_curve(p3, p1, self.iterations))
        
        # Convert to numpy array and separate x, y coordinates
        points = np.array(points)
        return points[:, 0], points[:, 1]

class SierpinskiTriangle(MathEquation):
    """Sierpinski triangle fractal.
    
    A fractal pattern of self-similar triangles.
    
    Parameters
    ----------
    iterations : int
        Number of iterations (default: 5)
    size : float
        Size of the triangle (default: 1.0)
    **kwargs : dict
        Additional parameters passed to MathEquation
    """
    
    def __init__(self, iterations=5, size=1.0, **kwargs):
        super().__init__(**kwargs)
        self.iterations = iterations
        self.size = size
    
    def _sierpinski(self, p1, p2, p3, iterations):
        if iterations == 0:
            return [p1, p2, p3, p1]
        
        # Calculate midpoints
        p1 = np.array(p1)
        p2 = np.array(p2)
        p3 = np.array(p3)
        
        m1 = (p1 + p2) / 2
        m2 = (p2 + p3) / 2
        m3 = (p3 + p1) / 2
        
        return (self._sierpinski(p1, m1, m3, iterations-1) +
                self._sierpinski(m1, p2, m2, iterations-1) +
                self._sierpinski(m3, m2, p3, iterations-1))
    
    def evaluate(self, t):
        # Create initial triangle
        p1 = np.array([0, 0])
        p2 = np.array([self.size, 0])
        p3 = np.array([self.size/2, self.size * np.sqrt(3)/2])
        
        # Generate points
        points = self._sierpinski(p1, p2, p3, self.iterations)
        
        # Convert to numpy array and separate x, y coordinates
        points = np.array(points)
        return points[:, 0], points[:, 1] 