from importlib.resources import files
import os
from pathlib import Path
from platformdirs import user_data_dir
from subprocess import run
import sys
from yaml import safe_load

from yamlpack import resources

_USER_CFG_PATH = Path(user_data_dir("yamlpack")) / "config"
_PACKAGE_RESOURCE_PATH = Path(str(files(resources)))

def get_local_resource(resource_path: str):
    return _USER_CFG_PATH / resource_path

def get_package_resource(resource_path: str):
    return _PACKAGE_RESOURCE_PATH / resource_path

def get_text(path: Path):
    if not path.is_file():
        return ""

    with path.open("r") as reader:
        return reader.read()

def load_yaml(path: Path) -> dict:
    return safe_load(get_text(path))

def open_file(filepath: str|Path):
    """Platform-agnostic file viewer, from https://stackoverflow.com/questions/17317219/"""
    if sys.platform == "win32":
        os.startfile(filepath)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        run([opener, filepath])