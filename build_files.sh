# build_files.sh
py -m pip install -r requirements.txt
py manage.py collectstatic --no-input
