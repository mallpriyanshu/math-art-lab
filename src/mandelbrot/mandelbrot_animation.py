import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

def create_custom_colormap():
    """Create a custom colormap for the visualization."""
    colors = ['#000000', '#1a1a2e', '#16213e', '#0f3460', '#533483', '#e94560']
    return LinearSegmentedColormap.from_list('custom', colors)

def generate_mandelbrot_frame(width, height, max_iter, current_iter):
    """Generate a single frame of the Mandelbrot set animation."""
    x = np.linspace(-2, 1, width)
    y = np.linspace(-1.5, 1.5, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(current_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def main():
    # Set up the figure
    plt.style.use('dark_background')  # Use dark background for better visibility
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.suptitle('Mandelbrot Set Generation', fontsize=16, color='white')
    
    # Initial parameters
    width, height = 800, 800
    max_iter = 100
    
    # Create initial image with proper normalization
    initial_data = np.zeros((height, width))
    img = ax.imshow(initial_data, 
                   cmap=create_custom_colormap(),
                   extent=[-2, 1, -1.5, 1.5],
                   vmin=0, vmax=max_iter)  # Set fixed color limits
    
    # Set up the plot
    ax.set_xlabel('Real', color='white')
    ax.set_ylabel('Imaginary', color='white')
    ax.tick_params(colors='white')
    
    # Add iteration counter
    iter_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white')
    
    def update(frame):
        """Update function for the animation."""
        # Generate frame
        divtime = generate_mandelbrot_frame(width, height, max_iter, frame)
        
        # Update image
        img.set_array(divtime)
        
        # Update iteration counter
        iter_text.set_text(f'Iteration: {frame}/{max_iter}')
        
        return [img, iter_text]
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=range(1, max_iter + 1),
                        interval=50, blit=True)
    
    # Ensure the plot is properly displayed
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 