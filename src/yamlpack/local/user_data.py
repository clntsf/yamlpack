from pathlib import Path
from platformdirs import user_data_dir
import re
from subprocess import run

from yamlpack.local.util import get_package_resource
from yamlpack.local.builders import add_builder

USER_DATA_DIR = Path(user_data_dir("yamlpack"))

def init_user_data():
    
    run(["mkdir", USER_DATA_DIR])

    # populate config dir
    run(["mkdir", USER_DATA_DIR / "config"])
    run(["cp", "-n", str(get_package_resource("settings.yml")), USER_DATA_DIR / "config" / "settings.yml"])

    # make builders dir and add default python builder
    run(["mkdir", USER_DATA_DIR / "builders"])
    add_builder("https://github.com/clntsf/builder-pypackage", "pypackage", quiet_fail=False)
 
if __name__ == "__main__":
    init_user_data()
    # update_builder("pypackage")