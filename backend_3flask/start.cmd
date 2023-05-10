python -m venv env
call env/scripts/activate
pip install -r requirements.txt
flask --app main run --host=0.0.0.0 --port=8003 --debug
cmd
