from yaml import safe_dump

from yamlpack.local.util import get_local_resource, get_package_resource, load_yaml

def _ensure_complete(settings: dict[str,str|dict], stub: str = ""):
    for key, value in settings.items():
        if isinstance(value, dict):
            _ensure_complete(value, stub + ("." if stub else "") + key)

        elif value is None:
            print(f"Missing config with setting name {stub}.{key}: null value")
            settings[key] = input("Enter replacement value: ")
            print()

    if stub == "":                  # toplevel, write to settings.yml
        update_settings(settings)

    return settings

def get_settings() -> dict[str, str|dict]:
    settings = load_yaml(get_local_resource("settings.yml"))
    _ensure_complete(settings)              # fill null fields
    return settings

def update_settings(settings: dict[str, str|dict]):
    file = get_local_resource("settings.yml")
    with open(file, "w") as writer:
        safe_dump(settings, writer)