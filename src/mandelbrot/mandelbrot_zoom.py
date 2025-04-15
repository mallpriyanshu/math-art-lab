import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

def create_custom_colormap():
    """Create a custom colormap for the visualization."""
    colors = ['#000000', '#1a1a2e', '#16213e', '#0f3460', '#533483', '#e94560']
    return LinearSegmentedColormap.from_list('custom', colors)

def generate_mandelbrot(width, height, x_min, x_max, y_min, y_max, max_iter=100):
    """Generate a Mandelbrot set for given coordinates."""
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    c = X + 1j * Y
    z = np.zeros_like(c)
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def main():
    # Set up the figure
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 10))
    fig.suptitle('Mandelbrot Set Zoom', fontsize=16, color='white')
    
    # Initial parameters
    width, height = 800, 800
    max_iter = 100
    
    # Define zoom path (center points and zoom levels)
    zoom_path = [
        # Start with full view
        {'x_min': -2.0, 'x_max': 1.0, 'y_min': -1.5, 'y_max': 1.5, 'zoom': 1},
        # Zoom into the main cardioid
        {'x_min': -0.8, 'x_max': -0.4, 'y_min': 0.1, 'y_max': 0.5, 'zoom': 2},
        # Zoom into a spiral
        {'x_min': -0.75, 'x_max': -0.73, 'y_min': 0.11, 'y_max': 0.13, 'zoom': 3},
        # Zoom into another interesting region
        {'x_min': -0.745, 'x_max': -0.743, 'y_min': 0.112, 'y_max': 0.114, 'zoom': 4},
        # Final zoom
        {'x_min': -0.7445, 'x_max': -0.7443, 'y_min': 0.1125, 'y_max': 0.1127, 'zoom': 5}
    ]
    
    # Create initial image
    initial_data = generate_mandelbrot(width, height, 
                                     zoom_path[0]['x_min'], zoom_path[0]['x_max'],
                                     zoom_path[0]['y_min'], zoom_path[0]['y_max'])
    img = ax.imshow(initial_data, 
                   cmap=create_custom_colormap(),
                   extent=[zoom_path[0]['x_min'], zoom_path[0]['x_max'],
                          zoom_path[0]['y_min'], zoom_path[0]['y_max']],
                   vmin=0, vmax=max_iter)
    
    # Set up the plot
    ax.set_xlabel('Real', color='white')
    ax.set_ylabel('Imaginary', color='white')
    ax.tick_params(colors='white')
    
    # Add zoom level counter
    zoom_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white')
    
    def update(frame):
        """Update function for the animation."""
        # Get current zoom parameters
        current = zoom_path[frame]
        
        # Generate frame
        divtime = generate_mandelbrot(width, height,
                                    current['x_min'], current['x_max'],
                                    current['y_min'], current['y_max'])
        
        # Update image
        img.set_array(divtime)
        img.set_extent([current['x_min'], current['x_max'],
                       current['y_min'], current['y_max']])
        
        # Update zoom level counter
        zoom_text.set_text(f'Zoom Level: {current["zoom"]}x')
        
        return [img, zoom_text]
    
    # Create animation
    anim = FuncAnimation(fig, update, frames=len(zoom_path),
                        interval=2000, blit=True)  # 2 seconds per frame
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 