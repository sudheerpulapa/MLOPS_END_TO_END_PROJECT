import os
from pathlib import Path

def create_empty_files(file_list):
    for filepath in file_list:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)
        if filedir and not os.path.exists(filedir):
            os.makedirs(filedir, exist_ok=True)

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass  # Create an empty file

if __name__ == "__main__":
    list_of_files = [
        ".github/workflows/ci.yaml",
        "src/__init__.py",
        "src/mongodb_connect/__init__.py",
        "src/mongodb_connect/mongo_crud.py",
        "tests/__init__.py",
        "tests/unit/__init__.py",
        "tests/integration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "setup.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini",
        "experiments/experiments.ipynb",
    ]

    create_empty_files(list_of_files)
