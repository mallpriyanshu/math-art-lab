"""
Artistic Examples

This script demonstrates how to create visually appealing mathematical art
using carefully chosen parameters. Each example is designed to create
beautiful, artistic patterns that showcase the mathematical beauty of
these equations.

To run this example:
1. Make sure you have matplotlib and numpy installed
2. Run this script: python artistic_examples.py
"""

import matplotlib
matplotlib.use('Agg')  # Use Agg backend for saving files without display
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from simple_equations import RoseCurve, LissajousCurve, HeartCurve, Spiral

# Create images directory if it doesn't exist
IMAGES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')
os.makedirs(IMAGES_DIR, exist_ok=True)

def create_flower_garden():
    """Create a beautiful collection of rose curves that resemble a flower garden."""
    # Create a figure with a dark background
    plt.figure(figsize=(12, 12), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Define beautiful color combinations
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEEAD']
    
    # Create multiple rose curves with carefully chosen parameters
    parameters = [
        (1.0, 5.0),   # 5-petal flower
        (1.2, 7.0),   # 7-petal flower
        (0.8, 3.0),   # 3-petal flower
        (1.5, 8.0),   # 8-petal flower
        (1.1, 6.0)    # 6-petal flower
    ]
    
    # Plot each rose curve with different colors and slight offsets
    for i, ((k, n), color) in enumerate(zip(parameters, colors)):
        rose = RoseCurve(k=k, n=n)
        x, y = rose.plot()
        # Add slight offset to each flower
        x += i * 0.5
        y += i * 0.5
        plt.plot(x, y, color=color, linewidth=3, alpha=0.8)
    
    plt.title('Mathematical Flower Garden', color='white', fontsize=16)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, 'flower_garden.png'), facecolor='black', bbox_inches='tight', dpi=300)
    plt.close()

def create_lissajous_art():
    """Create an artistic composition using Lissajous curves."""
    # Create a figure with a dark background
    plt.figure(figsize=(12, 12), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Define beautiful color combinations
    colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7']
    
    # Create multiple Lissajous curves with carefully chosen parameters
    parameters = [
        (3, 2, np.pi/4),    # Classic pattern
        (5, 4, np.pi/3),    # Complex pattern
        (7, 6, np.pi/2),    # Dense pattern
        (4, 3, np.pi/6),    # Medium complexity
        (6, 5, np.pi/5)     # Balanced pattern
    ]
    
    # Plot each Lissajous curve with different colors
    for (a, b, delta), color in zip(parameters, colors):
        lissajous = LissajousCurve(a=a, b=b, delta=delta)
        x, y = lissajous.plot()
        plt.plot(x, y, color=color, linewidth=2, alpha=0.7)
    
    plt.title('Lissajous Art Composition', color='white', fontsize=16)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, 'lissajous_art.png'), facecolor='black', bbox_inches='tight', dpi=300)
    plt.close()

def create_heart_composition():
    """Create an artistic composition using heart curves."""
    # Create a figure with a dark background
    plt.figure(figsize=(12, 12), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Define beautiful color combinations
    colors = ['#FF6B6B', '#FF8E8E', '#FFB5B5', '#FFD1D1', '#FFE3E3']
    
    # Create multiple heart curves with different scales and positions
    scales = [1.0, 0.8, 0.6, 0.4, 0.2]
    offsets = [(0, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    # Plot each heart curve with different colors and positions
    for scale, (dx, dy), color in zip(scales, offsets, colors):
        heart = HeartCurve(scale=scale)
        x, y = heart.plot()
        x += dx
        y += dy
        plt.plot(x, y, color=color, linewidth=3, alpha=0.8)
    
    plt.title('Heart Art Composition', color='white', fontsize=16)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, 'heart_art.png'), facecolor='black', bbox_inches='tight', dpi=300)
    plt.close()

def create_spiral_art():
    """Create an artistic composition using spirals."""
    # Create a figure with a dark background
    plt.figure(figsize=(12, 12), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')
    
    # Define beautiful color combinations
    colors = ['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB', '#B5EAD7']
    
    # Create multiple spirals with different growth rates and positions
    growth_rates = [0.05, 0.08, 0.12, 0.15, 0.2]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
    
    # Plot each spiral with different colors and rotations
    for growth_rate, angle, color in zip(growth_rates, angles, colors):
        spiral = Spiral(growth_rate=growth_rate)
        x, y = spiral.plot(t_range=(0, 8*np.pi), num_points=1000)
        # Rotate the spiral
        x_rot = x * np.cos(angle) - y * np.sin(angle)
        y_rot = x * np.sin(angle) + y * np.cos(angle)
        plt.plot(x_rot, y_rot, color=color, linewidth=2, alpha=0.7)
    
    plt.title('Spiral Art Composition', color='white', fontsize=16)
    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(os.path.join(IMAGES_DIR, 'spiral_art.png'), facecolor='black', bbox_inches='tight', dpi=300)
    plt.close()

def main():
    """Run all artistic examples."""
    print("Creating artistic mathematical patterns...")
    
    # Create flower garden
    print("\n1. Creating a mathematical flower garden...")
    create_flower_garden()
    
    # Create Lissajous art
    print("\n2. Creating Lissajous art composition...")
    create_lissajous_art()
    
    # Create heart composition
    print("\n3. Creating heart art composition...")
    create_heart_composition()
    
    # Create spiral art
    print("\n4. Creating spiral art composition...")
    create_spiral_art()
    
    print(f"\nAll artistic examples completed! Images saved in: {IMAGES_DIR}")

if __name__ == "__main__":
    main() 