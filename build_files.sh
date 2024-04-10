#!/bin/bash

# Install pip if not available (requires sudo)
# sudo apt update
# sudo apt install python3-pip

# Use Python provided by Vercel, which should already have pip
python3 -m pip install -r requirements.txt

# Make migrations and collect static files
python3 manage.py collectstatic --no-input