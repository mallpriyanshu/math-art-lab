"""
Simple Examples for Beginners

This script shows how to use the basic mathematical equations
to create simple plots. It's perfect for beginners who want to
learn about mathematical art.

To run this example:
1. Make sure you have matplotlib and numpy installed
2. Run this script: python simple_examples.py
"""

import matplotlib.pyplot as plt
import numpy as np
from ..simple_equations import Circle, Spiral

def plot_circle():
    """Create and plot a simple circle."""
    # Create a circle with radius 2
    circle = Circle(radius=2)
    
    # Get the x and y coordinates
    x, y = circle.plot()
    
    # Create the plot
    plt.figure(figsize=(6, 6))
    plt.plot(x, y, 'b-', linewidth=2)
    plt.title('Simple Circle')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def plot_spiral():
    """Create and plot a simple spiral."""
    # Create a spiral with growth rate 0.1
    spiral = Spiral(growth_rate=0.1)
    
    # Get the x and y coordinates (using more points for smoother spiral)
    x, y = spiral.plot(t_range=(0, 8*np.pi), num_points=1000)
    
    # Create the plot
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, 'r-', linewidth=2)
    plt.title('Simple Spiral')
    plt.axis('equal')
    plt.grid(True)
    plt.show()

def main():
    """Run all examples."""
    print("Running simple examples...")
    
    # Plot a circle
    print("\n1. Plotting a circle...")
    plot_circle()
    
    # Plot a spiral
    print("\n2. Plotting a spiral...")
    plot_spiral()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main() 