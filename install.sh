#!/bin/bash

#Creates a virtual environment in the directory 
echo "[x] Creating a new virtual environment in the current directory"
python3 -m venv venv

echo "[x] Acivating the new virtual environment named [venv]"
./venv/bin/activate

echo "[x] Installing packages for the project"
# install the packages using pip
pip install -r requirements.txt

echo "[x] Initializing the Project and creating database "
# Create database for the products 
python -c "from main import db, create_app; db.create_all(app=create_app())"

echo "[x] Starting Server"
# Starts the server
python3 main.py