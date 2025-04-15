import numpy as np
import matplotlib.pyplot as plt
from src.math_art import generate_parametric_art
from src.mandelbrot import generate_mandelbrot

def create_custom_art():
    # Example 1: Parametric Art
    def custom_parametric(t):
        # Custom parametric equations
        x = np.sin(3*t) * np.cos(2*t)
        y = np.sin(4*t) * np.cos(3*t)
        return x, y
    
    # Generate parametric art
    fig, ax = plt.subplots(figsize=(10, 10))
    t = np.linspace(0, 2*np.pi, 1000)
    x, y = custom_parametric(t)
    ax.plot(x, y, 'b-', linewidth=2)
    ax.set_title('Custom Parametric Art')
    ax.axis('equal')
    plt.savefig('custom_parametric.png')
    plt.close()
    
    # Example 2: Mandelbrot with custom parameters
    mandelbrot_img = generate_mandelbrot(
        width=800,
        height=800,
        x_min=-2.0,
        x_max=1.0,
        y_min=-1.5,
        y_max=1.5,
        max_iterations=100
    )
    plt.imshow(mandelbrot_img, cmap='hot')
    plt.axis('off')
    plt.savefig('custom_mandelbrot.png')
    plt.close()

if __name__ == "__main__":
    create_custom_art() 