# build_files.sh
# shellcheck disable=SC2034
python_path="C:\Users\Ailoe\AppData\Local\Programs\Python\Python312\Scripts\python.exe"

"C:\Users\Ailoe\AppData\Local\Programs\Python\Python312\Scripts\python.exe" -m pip install -r requirements.txt
"C:\Users\Ailoe\AppData\Local\Programs\Python\Python312\Scripts\python.exe" manage.py collectstatic --no-input
