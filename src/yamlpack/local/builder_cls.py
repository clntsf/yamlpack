from typing import Protocol
from pathlib import Path

class Builder(Protocol):

    @staticmethod
    def build(package_fp: Path, settings: dict): ...
    