"""
Advanced Examples for Beginners

This script shows how to use the more advanced mathematical equations
to create beautiful patterns. It demonstrates how changing parameters
affects the final result.

To run this example:
1. Make sure you have matplotlib and numpy installed
2. Run this script: python advanced_examples.py
"""

import matplotlib.pyplot as plt
import numpy as np
from ..simple_equations import RoseCurve, LissajousCurve, HeartCurve

def plot_rose_curves():
    """Create and plot different rose curves with varying parameters."""
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Rose Curves with Different Parameters', fontsize=16)
    
    # Different parameters for rose curves
    parameters = [
        (1.0, 2.0),  # 2 petals
        (1.0, 3.0),  # 3 petals
        (1.0, 4.0),  # 4 petals
        (1.0, 5.0)   # 5 petals
    ]
    
    for i, (k, n) in enumerate(parameters):
        # Create the rose curve
        rose = RoseCurve(k=k, n=n)
        x, y = rose.plot()
        
        # Plot on the appropriate subplot
        ax = axes[i//2, i%2]
        ax.plot(x, y, 'b-', linewidth=2)
        ax.set_title(f'k={k}, n={n}')
        ax.axis('equal')
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

def plot_lissajous_curves():
    """Create and plot different Lissajous curves with varying parameters."""
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Lissajous Curves with Different Parameters', fontsize=16)
    
    # Different parameters for Lissajous curves
    parameters = [
        (3, 2, np.pi/2),  # Classic Lissajous
        (3, 2, 0),        # No phase difference
        (4, 3, np.pi/2),  # Different frequency ratio
        (5, 4, np.pi/4)   # Different phase difference
    ]
    
    for i, (a, b, delta) in enumerate(parameters):
        # Create the Lissajous curve
        lissajous = LissajousCurve(a=a, b=b, delta=delta)
        x, y = lissajous.plot()
        
        # Plot on the appropriate subplot
        ax = axes[i//2, i%2]
        ax.plot(x, y, 'r-', linewidth=2)
        ax.set_title(f'a={a}, b={b}, δ={delta:.2f}')
        ax.axis('equal')
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

def plot_heart_curves():
    """Create and plot heart curves with different scales."""
    # Create a figure with multiple subplots
    fig, axes = plt.subplots(2, 2, figsize=(12, 12))
    fig.suptitle('Heart Curves with Different Scales', fontsize=16)
    
    # Different scales for heart curves
    scales = [0.5, 1.0, 1.5, 2.0]
    
    for i, scale in enumerate(scales):
        # Create the heart curve
        heart = HeartCurve(scale=scale)
        x, y = heart.plot()
        
        # Plot on the appropriate subplot
        ax = axes[i//2, i%2]
        ax.plot(x, y, 'm-', linewidth=2)
        ax.set_title(f'Scale = {scale}')
        ax.axis('equal')
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

def main():
    """Run all advanced examples."""
    print("Running advanced examples...")
    
    # Plot rose curves
    print("\n1. Plotting rose curves with different parameters...")
    plot_rose_curves()
    
    # Plot Lissajous curves
    print("\n2. Plotting Lissajous curves with different parameters...")
    plot_lissajous_curves()
    
    # Plot heart curves
    print("\n3. Plotting heart curves with different scales...")
    plot_heart_curves()
    
    print("\nAll examples completed!")

if __name__ == "__main__":
    main() 