from importlib.resources import read_text
from pathlib import Path
from subprocess import run
from sys import argv
from yaml import safe_load

from . import resources

def load_data(resource_path: str) -> dict:
    """Load a yaml file from resources with given filepath"""
    text = read_text(resources, resource_path)
    return safe_load(text)

def _init_module(path: Path):
    """Make a module folder and __init__.py file (dummy module contents)"""
    run(["mkdir", path])
    run(["touch", f"{path}/__init__.py"])

def _build_modules(path: Path, modules: list):
    """
    build modules recursively from structure specified in the YAML config
    """

    for module in modules:
        if isinstance(module, str):
            _init_module(Path.joinpath(path, module))

        elif isinstance(module, dict):
            module_name = list(module.keys())[0]
            module_path = Path.joinpath(path, module_name)
            _init_module(module_path)
            _build_modules(module_path, module[module_name])

def main(package_yaml_fp: str, package_fp: str|Path):
    
    settings = load_data("settings.yml")
    package_cfg = load_data(package_yaml_fp)

    name = package_cfg["name"]
    description = package_cfg["description"]
    modules: list[str|dict] = package_cfg["modules"]

    package_abspath = Path(package_fp).resolve()

    srcpath = package_abspath.joinpath(f"src/{name}")
    run(["mkdir", f"{package_abspath}/src"])
    run(["mkdir", srcpath])
    _build_modules(srcpath, modules)

if __name__ == "__main__":
    main(argv[1], ".")