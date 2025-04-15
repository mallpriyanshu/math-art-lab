"""
Simple Mathematical Equations

This module provides some basic mathematical equations that are easy to understand
and perfect for beginners learning about mathematical art.

Example:
    circle = Circle(radius=2)
    x, y = circle.plot()
    plt.plot(x, y)
    plt.show()
"""

import numpy as np
from base_equation import BaseEquation

class Circle(BaseEquation):
    """
    A simple circle equation.
    
    This class creates a perfect circle using parametric equations.
    It's one of the simplest mathematical curves to understand.
    
    Attributes:
        radius (float): The radius of the circle
    """
    
    def __init__(self, radius=1.0):
        """
        Initialize a circle with given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        super().__init__(
            name="Circle",
            description="A perfect circle using parametric equations"
        )
        self.radius = radius
    
    def evaluate(self, t):
        """
        Calculate x and y coordinates for a circle.
        
        The equations are:
        x = radius * cos(t)
        y = radius * sin(t)
        
        Args:
            t (numpy.ndarray): Array of angle values in radians
            
        Returns:
            tuple: (x, y) coordinates
        """
        x = self.radius * np.cos(t)
        y = self.radius * np.sin(t)
        return x, y

class Spiral(BaseEquation):
    """
    A simple spiral equation.
    
    This class creates a spiral that grows outward as the angle increases.
    It demonstrates how to create more complex curves by modifying
    the basic circle equations.
    
    Attributes:
        growth_rate (float): How quickly the spiral grows outward
    """
    
    def __init__(self, growth_rate=0.1):
        """
        Initialize a spiral with given growth rate.
        
        Args:
            growth_rate (float): How quickly the spiral grows outward
        """
        super().__init__(
            name="Spiral",
            description="A spiral that grows outward as the angle increases"
        )
        self.growth_rate = growth_rate
    
    def evaluate(self, t):
        """
        Calculate x and y coordinates for a spiral.
        
        The equations are:
        r = growth_rate * t
        x = r * cos(t)
        y = r * sin(t)
        
        Args:
            t (numpy.ndarray): Array of angle values in radians
            
        Returns:
            tuple: (x, y) coordinates
        """
        r = self.growth_rate * t
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y 

class RoseCurve(BaseEquation):
    """
    A rose curve (rhodonea curve) equation.
    
    This creates beautiful flower-like patterns using trigonometric functions.
    The number of petals depends on the parameters k and n.
    
    Attributes:
        k (float): Controls the size of the petals
        n (float): Controls the number of petals
    """
    
    def __init__(self, k=1.0, n=3.0):
        """
        Initialize a rose curve with given parameters.
        
        Args:
            k (float): Controls the size of the petals
            n (float): Controls the number of petals
        """
        super().__init__(
            name="Rose Curve",
            description="A beautiful flower-like pattern using trigonometric functions"
        )
        self.k = k
        self.n = n
    
    def evaluate(self, t):
        """
        Calculate x and y coordinates for a rose curve.
        
        The equations are:
        r = k * cos(n * t)
        x = r * cos(t)
        y = r * sin(t)
        
        Args:
            t (numpy.ndarray): Array of angle values in radians
            
        Returns:
            tuple: (x, y) coordinates
        """
        r = self.k * np.cos(self.n * t)
        x = r * np.cos(t)
        y = r * np.sin(t)
        return x, y

class LissajousCurve(BaseEquation):
    """
    A Lissajous curve equation.
    
    This creates interesting patterns by combining two sine waves
    with different frequencies. The pattern depends on the ratio
    of the frequencies (a/b).
    
    Attributes:
        a (float): Frequency in x-direction
        b (float): Frequency in y-direction
        delta (float): Phase difference between x and y
    """
    
    def __init__(self, a=3.0, b=2.0, delta=np.pi/2):
        """
        Initialize a Lissajous curve with given parameters.
        
        Args:
            a (float): Frequency in x-direction
            b (float): Frequency in y-direction
            delta (float): Phase difference between x and y
        """
        super().__init__(
            name="Lissajous Curve",
            description="A pattern created by combining two sine waves"
        )
        self.a = a
        self.b = b
        self.delta = delta
    
    def evaluate(self, t):
        """
        Calculate x and y coordinates for a Lissajous curve.
        
        The equations are:
        x = sin(a * t)
        y = sin(b * t + delta)
        
        Args:
            t (numpy.ndarray): Array of angle values in radians
            
        Returns:
            tuple: (x, y) coordinates
        """
        x = np.sin(self.a * t)
        y = np.sin(self.b * t + self.delta)
        return x, y

class HeartCurve(BaseEquation):
    """
    A heart-shaped curve equation.
    
    This creates a simple heart shape using parametric equations.
    It's a fun example that shows how to create more complex shapes.
    
    Attributes:
        scale (float): Controls the size of the heart
    """
    
    def __init__(self, scale=1.0):
        """
        Initialize a heart curve with given scale.
        
        Args:
            scale (float): Controls the size of the heart
        """
        super().__init__(
            name="Heart Curve",
            description="A simple heart shape using parametric equations"
        )
        self.scale = scale
    
    def evaluate(self, t):
        """
        Calculate x and y coordinates for a heart curve.
        
        The equations are:
        x = scale * 16 * sin(t)^3
        y = scale * (13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t))
        
        Args:
            t (numpy.ndarray): Array of angle values in radians
            
        Returns:
            tuple: (x, y) coordinates
        """
        x = self.scale * 16 * np.sin(t)**3
        y = self.scale * (13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t))
        return x, y 