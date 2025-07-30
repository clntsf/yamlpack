from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from platformdirs import user_data_dir

def load_builder(name: str):
    init_path = Path(user_data_dir("yamlpack")) / f"builders/{name}/__init__.py"
    print(init_path)

load_builder("myfoo")