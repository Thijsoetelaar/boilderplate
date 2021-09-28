
# Sources

1. Setup: https://towardsdatascience.com/best-practices-for-setting-up-a-python-environment-d4af439846a
2. Python packaging: https://packaging.python.org/tutorials/packaging-projects/


# Setting up 

```bash 
pyenv local 3.9.0
poetry init
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