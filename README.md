
# Sources

1. Setup: https://towardsdatascience.com/best-practices-for-setting-up-a-python-environment-d4af439846a
2. Python packaging: https://packaging.python.org/tutorials/packaging-projects/
3. Poetry: https://python-poetry.org/docs/cli/


# Setting up 

```bash 
pyenv local 3.9.0
poetry init
poetry install
poetry shell
poetry add --dev pytest
poetry add -vvv pandas
poetry export -f requirements.txt --output requirements.txt

```

# Building package

```bash 
python3 -m build
```

# Testing
```bash 
poetry run pytest -vv
```

# Git 

Create a .gitignore file here: https://www.toptal.com/developers/gitignore


# Vscode & Git

https://github.com/romkatv/powerlevel10k/issues/671

# CURL example

```bash
python app.py                                                                                 -
curl -X POST http://192.168.2.105:8080/add -H "Content-Type: application/json" -d '{"number": '5'}'
curl -X POST http://192.168.2.105:8080/predict -H "Content-Type: application/json" -d '{"age": 55,"job": 5, "credit_amount": 55}'
curl -X POST http://192.168.2.105:8080/predict -H "Content-Type: application/json" -d @example.json
```

# Docker 

1. First build your docker image 
2. then run and publish on the correct port 
3. Test both endpoints `/add` and `/predict`

```bash 
docker build -t example_package .   
docker run --publish 8080:8080 example_package
curl http://localhost:8080/add -H "Content-Type: application/json" -d '{"number": '5'}'
curl http://localhost:8080/predict -H "Content-Type: application/json" -d @example.json
```

# Train 

This trains a logistic regression model with csv file as input that is in the `\data` folder

```bash 
python train.py --csv "data.csv"
```