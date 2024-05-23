from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='DiamondPricePrediction',
    version='0.1.0',
    author='Sudheer Pulapa',
    author_email='sudheerpulapa@gmail.com',
    description='A package for predicting diamond prices',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/DiamondPricePrediction",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/DiamondPricePrediction/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "scikit-learn",
        "pandas",
        "numpy",
    ],
)
