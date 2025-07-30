from importlib.resources import files
from pathlib import Path
from platformdirs import user_data_dir
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