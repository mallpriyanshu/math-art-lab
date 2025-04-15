from src.equations import (
    RoseCurve,
    ButterflyCurve,
    MandelbrotSet,
    JuliaSet,
    KochSnowflake,
    SierpinskiTriangle
)

# Test imports
print("All imports successful!")

# Test creating a rose curve
rose = RoseCurve(n=5, d=8)
x, y = rose.generate_points()
print(f"Rose curve generated with {len(x)} points")

# Test creating a butterfly curve
butterfly = ButterflyCurve(amplitude=2.0)
x, y = butterfly.generate_points()
print(f"Butterfly curve generated with {len(x)} points")

# Test creating a Mandelbrot set
mandelbrot = MandelbrotSet(width=400, height=400)
fractal = mandelbrot.evaluate(None)
print(f"Mandelbrot set generated with shape {fractal.shape}")

# Test creating a Julia set
julia = JuliaSet(width=400, height=400)
fractal = julia.evaluate(None)
print(f"Julia set generated with shape {fractal.shape}")

# Test creating a Koch snowflake
snowflake = KochSnowflake(iterations=4)
x, y = snowflake.generate_points()
print(f"Koch snowflake generated with {len(x)} points")

# Test creating a Sierpinski triangle
triangle = SierpinskiTriangle(iterations=5)
x, y = triangle.generate_points()
print(f"Sierpinski triangle generated with {len(x)} points")

print("\nAll tests completed successfully!") 