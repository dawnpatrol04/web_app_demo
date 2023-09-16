#!/bin/bash
# Create a virtual environment
python3 -m venv .venv
# Activate the virtual environment
source .venv/bin/activate
# Upgrade pip
pip install --upgrade pip
# Install necessary packages
pip install -r requirements.txt
