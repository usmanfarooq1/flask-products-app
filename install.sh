#!/bin/bash

#Creates a virtual environment in the directory 
python3 -m venv venv
source venv/bin/activate

# install the packages using pip
pip install -r requirements.txt

# Create database for the products 
python -c "from main import db, create_app; db.create_all(app=create_app())"

# Starts the server
python3 main.py