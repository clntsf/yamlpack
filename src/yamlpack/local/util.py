from importlib.resources import files
from yaml import safe_load

from yamlpack import resources

def get_resource(resource_path: str):
    return files(resources) / resource_path

def get_text(resource_path: str):
    with get_resource(resource_path).open("r") as reader:
        return reader.read()

def load_yaml(resource_path: str) -> dict:
    """Load a yaml file from resources with given filepath"""
    resource = get_resource(resource_path)
    if not resource.is_file():
        return {}
    
    with resource.open("r") as reader:
        return safe_load(reader.read())