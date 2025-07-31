from pathlib import Path
from platformdirs import user_data_dir
import re
from subprocess import run

from yamlpack.local.util import get_package_resource
from yamlpack.local.builders import add_builder, update_builder

USER_DATA_DIR = Path(user_data_dir("yamlpack"))

def init_user_data():
    
    if USER_DATA_DIR.exists():
        print("[@init]: user data directory exists; skipping creation")
    else:
        run(["mkdir", USER_DATA_DIR])

    # populate config dir
    config_path = USER_DATA_DIR / "config"
    if config_path.exists():
        print("[@init]: user config folder exists; skipping creation")
    else:
        run(["mkdir", config_path])

    run(["cp", "-n", str(get_package_resource("settings.yml")), config_path / "settings.yml"])

    # make builders dir and add default python builder
    builders_path = USER_DATA_DIR / "builders"
    if builders_path.exists():
        print("[@init]: builders folder exists; skipping creation")
    else:
        run(["mkdir", "-p", builders_path])


    if (builders_path / "pypackage").exists():
        print("[@init] default builder 'pypackage' is installed, pulling to update instead")
        update_builder("pypackage")
    else:
        add_builder("https://github.com/clntsf/builder-pypackage", "pypackage", quiet_fail=False)
 
if __name__ == "__main__":
    init_user_data()
    # update_builder("pypackage")