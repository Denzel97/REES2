# build_files.sh
.\venv\Scripts\activate  # Activate virtual environment
python -m pip install -r requirements.txt
python3.9 manage.py collectstatic --no-input
