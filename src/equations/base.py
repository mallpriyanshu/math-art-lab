import numpy as np
from abc import ABC, abstractmethod

class MathEquation(ABC):
    """Base class for all mathematical equations."""
    
    def __init__(self, t_range=(0, 2*np.pi), num_points=1000):
        self.t_range = t_range
        self.num_points = num_points
        self.t = np.linspace(t_range[0], t_range[1], num_points)
    
    @abstractmethod
    def evaluate(self, t):
        """Evaluate the equation at parameter t."""
        pass
    
    def generate_points(self):
        """Generate points for the entire parameter range."""
        return self.evaluate(self.t)
    
    def transform(self, scale=1.0, rotation=0.0, translation=(0, 0)):
        """Apply transformations to the equation."""
        x, y = self.generate_points()
        
        # Apply rotation
        if rotation != 0:
            x_rot = x * np.cos(rotation) - y * np.sin(rotation)
            y_rot = x * np.sin(rotation) + y * np.cos(rotation)
            x, y = x_rot, y_rot
        
        # Apply scaling
        x *= scale
        y *= scale
        
        # Apply translation
        x += translation[0]
        y += translation[1]
        
        return x, y 