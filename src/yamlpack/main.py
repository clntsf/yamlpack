from pathlib import Path
from subprocess import run
from sys import argv
from yaml import safe_load

from yamlpack.local.settings import get_settings
from yamlpack.local.util import get_text

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

def fill_fields(text: str, settings: dict):
    map = [
        ("@AUTHORNAME", settings["user"]["fullname"]),
        ("@AUTHOREMAIL", settings["user"]["email"]),
        ("@GITHUB", "https://github.com/" + settings["user"]["github"]),
        ("@PKGNAME", settings["package"]["name"]),
        ("@DESCRIPTION", settings["package"]["description"]),
    ]

    for (old, new) in map:
        text = text.replace(old, new)
    
    return text

def _populate_package_info_files(
        package_path: Path,
        settings: dict[str, str|dict],
    ):

    pyproject_txt = get_text("pyproject.toml.sample")
    license_txt = get_text("LICENSE.sample")
    setup_txt = get_text("setup.py.sample")

    with open(package_path.joinpath("pyproject.toml"), "w") as writer:
        writer.write(fill_fields(pyproject_txt, settings))

    with open(package_path.joinpath("LICENSE"), "w") as writer:
        writer.write(fill_fields(license_txt, settings))

    with open(package_path.joinpath("setup.py"), "w") as writer:
        writer.write(fill_fields(setup_txt, settings))


def main(package_yaml_fp: str, package_fp: str|Path):
    
    settings = get_settings()
    with open(package_yaml_fp, "r") as reader:
        package_cfg = safe_load(reader)

    name = package_cfg["name"]

    package_abspath = Path(package_fp).resolve()

    settings["package"] = package_cfg
    _populate_package_info_files(package_abspath, settings)

    srcpath = package_abspath.joinpath(f"src/{name}")
    run(["mkdir", f"{package_abspath}/src"])
    _init_module(srcpath)

    modules: list[str|dict] = package_cfg["modules"]
    _build_modules(srcpath, modules)

    boilerplate = ["README.md", ".gitignore", f"src/{name}/__main__.py"]
    for filepath in boilerplate:
        run(["touch", f"{package_abspath}/{filepath}"])

if __name__ == "__main__":
    main(argv[1], ".")