from setuptools import setup, find_packages

setup(
    name="math-art-lab",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "pillow>=8.0.0",
    ],
    description="A Python library for creating beautiful mathematical art through parametric equations and fractals",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/math-art-lab",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Artistic Software",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
) 