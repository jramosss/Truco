alias run="uvicorn main:app --reload"
alias venv="workon truco"
alias test="python -m pytest -s; rm testing_db.sqlite3"
alias cov="coverage run -m pytest; coverage report; rm testing_db.sqlite3"

venv