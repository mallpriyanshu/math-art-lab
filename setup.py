from setuptools import setup, find_packages

setup(
    name="math-art",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "pillow>=8.0.0",
    ],
) 