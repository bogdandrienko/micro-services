python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host=0.0.0.0 --port=8004
sh
