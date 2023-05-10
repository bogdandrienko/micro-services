python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
flask --app main run --host=0.0.0.0 --port=8003 --debug
sh
