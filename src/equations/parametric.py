import numpy as np
from .base import MathEquation

class Circle(MathEquation):
    """Parametric equation for a circle."""
    def __init__(self, radius=1.0, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
    
    def evaluate(self, t):
        x = self.radius * np.cos(t)
        y = self.radius * np.sin(t)
        return x, y

class Spiral(MathEquation):
    """Parametric equation for a spiral."""
    def __init__(self, growth_rate=1.0, **kwargs):
        super().__init__(**kwargs)
        self.growth_rate = growth_rate
    
    def evaluate(self, t):
        r = self.growth_rate * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

class RoseCurve(MathEquation):
    """Parametric equation for a rose curve (rhodonea curve)."""
    def __init__(self, n=5, d=8, **kwargs):
        super().__init__(**kwargs)
        self.n = n
        self.d = d
    
    def evaluate(self, t):
        r = np.cos(self.n/self.d * t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

class HeartCurve(MathEquation):
    """Parametric equation for a heart-shaped curve."""
    def evaluate(self, t):
        x = 16 * np.sin(t)**3
        y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
        return x, y

class LissajousCurve(MathEquation):
    """Parametric equation for a Lissajous curve."""
    def __init__(self, a=3, b=2, delta=np.pi/2, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b
        self.delta = delta
    
    def evaluate(self, t):
        x = np.sin(self.a * t + self.delta)
        y = np.sin(self.b * t)
        return x, y

class ButterflyCurve(MathEquation):
    """Butterfly curve equation.
    
    A beautiful parametric curve that resembles a butterfly.
    
    Parameters
    ----------
    amplitude : float
        Amplitude of the curve (default: 1.0)
    **kwargs : dict
        Additional parameters passed to MathEquation
    """
    
    def __init__(self, amplitude=1.0, **kwargs):
        super().__init__(**kwargs)
        self.amplitude = amplitude
    
    def evaluate(self, t):
        x = self.amplitude * np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
        y = self.amplitude * np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) - np.sin(t/12)**5)
        return x, y

class TrefoilKnot(MathEquation):
    """Trefoil knot equation.
    
    A mathematical knot that forms a three-lobed shape.
    
    Parameters
    ----------
    radius : float
        Radius of the knot (default: 1.0)
    **kwargs : dict
        Additional parameters passed to MathEquation
    """
    
    def __init__(self, radius=1.0, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
    
    def evaluate(self, t):
        x = self.radius * (np.sin(t) + 2 * np.sin(2*t))
        y = self.radius * (np.cos(t) - 2 * np.cos(2*t))
        return x, y 