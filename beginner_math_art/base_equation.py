"""
Base Equation Class for Mathematical Art

This module provides a simple base class for creating mathematical equations.
It's designed to be easy to understand and extend for beginners.

Example:
    class MyEquation(BaseEquation):
        def evaluate(self, t):
            x = t * np.cos(t)
            y = t * np.sin(t)
            return x, y
"""

import numpy as np

class BaseEquation:
    """
    A base class for creating mathematical equations.
    
    This class provides the basic structure for creating mathematical art.
    To create your own equation, inherit from this class and implement
    the evaluate() method.
    
    Attributes:
        name (str): The name of the equation
        description (str): A brief description of what the equation does
    """
    
    def __init__(self, name="Base Equation", description="A basic mathematical equation"):
        """
        Initialize the equation with a name and description.
        
        Args:
            name (str): The name of the equation
            description (str): A brief description of what the equation does
        """
        self.name = name
        self.description = description
    
    def evaluate(self, t):
        """
        Evaluate the equation at given parameter values.
        
        This method must be implemented by subclasses.
        It should return x and y coordinates for plotting.
        
        Args:
            t (numpy.ndarray): Array of parameter values
            
        Returns:
            tuple: (x, y) coordinates as numpy arrays
            
        Raises:
            NotImplementedError: If the method is not implemented by a subclass
        """
        raise NotImplementedError("Subclasses must implement evaluate()")
    
    def plot(self, t_range=(0, 2*np.pi), num_points=1000):
        """
        Create a simple plot of the equation.
        
        Args:
            t_range (tuple): The range of t values to plot (start, end)
            num_points (int): Number of points to use in the plot
            
        Returns:
            tuple: (x, y) coordinates for plotting
        """
        t = np.linspace(t_range[0], t_range[1], num_points)
        return self.evaluate(t) 