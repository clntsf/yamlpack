from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from platformdirs import user_data_dir
import re
from subprocess import run, check_call, CalledProcessError
import sys

from yamlpack.local.builder_cls import Builder

USER_DATA_DIR = Path(user_data_dir("yamlpack"))
_BUILDER_NAME_RE = r"https:\/\/.*?\/(.+?).git"


class BuilderNotFoundException(Exception):
    def __init__(self, name: str):
        super().__init__(f"Builder {name} not found")

class BuilderRemoteNotResolvedException(Exception):
    def __init__(self, remote: str):
        super().__init__(f"Remote {remote} could not be resolved")

def load_builder(name: str) -> Builder:
    package_path = USER_DATA_DIR / f"builders/{name}"
    init_path = package_path / "__init__.py"
    if not init_path.exists():
        raise BuilderNotFoundException(name)
    
    spec = spec_from_file_location(
        "builder", init_path, submodule_search_locations=[str(package_path)]
    )
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load builder {name}")
    
    module = module_from_spec(spec)
    sys.modules["builder"] = module
    spec.loader.exec_module(module)

    return module

def add_builder(builder_repo_link: str, name: str|None = None, quiet_fail: bool = False):

    if name is None:
        reponame = re.match(_BUILDER_NAME_RE, builder_repo_link)
        if reponame is None:
            raise BuilderRemoteNotResolvedException(builder_repo_link)

        name = reponame.group()

    # TODO: on top of this, because this is going to go into the CLI we should
    # really just return a status message and ignore it in init_user_data
    try:
        check_call(["git", "clone", builder_repo_link, USER_DATA_DIR / "builders" / name])
    except CalledProcessError as cpe:
        if quiet_fail: return

        if cpe.stderr is not None and "already exists" in cpe.stderr:
            print(f"[WARN]: A builder with this name has already been initiated. Did you mean to update it?")

        elif cpe.stderr is not None and "could not resolve host" in cpe.stderr:
            raise BuilderRemoteNotResolvedException(builder_repo_link)

        else:
            raise cpe   # the error is of some other variety, reraise it


def update_builder(builder_name: str):

    builder_dir = USER_DATA_DIR / "builders" / builder_name
    if not builder_dir.exists():
        raise BuilderNotFoundException(builder_name)

    
    print(f"Updating builder: {builder_name}")
    run(["git", "pull"], cwd=builder_dir)


def delete_builder(builder_name: str):
    name_sanitized = Path(builder_name).name    # prevent relative path injection :)
    builder_path = USER_DATA_DIR / "builders" / name_sanitized

    if builder_path.exists():
        print(f"Deleting Builder: {builder_name}")
        run(["rm", "-rf", builder_path])

    else:
        raise BuilderNotFoundException(builder_name)