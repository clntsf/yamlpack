from pathlib import Path
from yaml import safe_load

from yamlpack.local.settings import get_settings
from yamlpack.local.builders import load_builder

def make_pack(package_path: str, schema_path: str):
    
    settings = get_settings()
    with open(schema_path, "r") as reader:
        package_cfg: dict = safe_load(reader)

    settings["package"] = package_cfg

    builder = load_builder(package_cfg.get("builder", "pypackage"))
    builder.build(Path(package_path), settings)