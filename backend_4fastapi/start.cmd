python -m venv env
call env/scripts/activate
pip install -r requirements.txt
uvicorn main:app --reload --host=0.0.0.0 --port=8004
cmd
