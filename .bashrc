alias run="uvicorn main:app --reload"
alias venv="source .venv/bin/activate"
alias test="python -m pytest -s $1; rm testing_db.sqlite3"

venv