#!/bin/bash

echo "$(date): START"

echo "$(date): Creating environment with Python 3.8 version"

# Create a virtual environment named 'env' with Python 3.8
conda create --prefix ./env python=3.8 -y

echo "$(date): Activating the environment"

# Activate the created environment
source activate ./env

echo "$(date): Installing the development requirements"

# Install the development requirements
pip install -r requirements_dev.txt

echo "$(date): END"
