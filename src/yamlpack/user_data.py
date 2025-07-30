from pathlib import Path
from platformdirs import user_data_dir
import re
from subprocess import run

from yamlpack.util import get_resource

USER_DATA_DIR = Path(user_data_dir("yamlpack"))
_BUILDER_NAME_RE = r"https:\/\/.*?\/(.+?).git"

def init_user_data():
    
    run(["mkdir", USER_DATA_DIR])

    # populate config dir
    run(["mkdir", USER_DATA_DIR / "config"])
    run(["cp", "-n", str(get_resource("settings.yml")), "config/settings.yml"])

    # make builders dir and add basic python builder
    run(["mkdir", USER_DATA_DIR / "builders"])
    add_builder("https://github.com/clntsf/builder-pypackage")


def add_builder(builder_repo_link: str, name: str|None = None):
    if name is None:
        reponame = re.match(_BUILDER_NAME_RE, builder_repo_link)
        if reponame is None:
            raise ValueError("Invalid builder link provided: does your link point to the top-level of a git repository?")

        name = reponame.group()

    run(["git", "clone", builder_repo_link, USER_DATA_DIR / f"builders/{name}"])