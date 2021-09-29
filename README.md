
# Sources

1. Setup: https://towardsdatascience.com/best-practices-for-setting-up-a-python-environment-d4af439846a
2. Python packaging: https://packaging.python.org/tutorials/packaging-projects/


# Setting up 

```bash 
pyenv local 3.9.0
poetry init
poetry install
poetry shell
poetry add --dev pytest
poetry add pandas

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
curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"number": '5'}'
```

# Docker 

```bash 
docker build -t example_package .   
docker run --publish 8080:8080 example_package
curl http://localhost:8080/add -H "Content-Type: application/json" -d '{"number": '5'}'
```