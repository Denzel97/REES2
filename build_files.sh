# build_files.sh
# shellcheck disable=SC2034
python_path="C:\Users\Ailoe\AppData\Local\Programs\Python\Python312\Scripts\python.exe"

python -m pip install -r requirements.txt
python manage.py collectstatic --no-input
