from typing import Protocol
from pathlib import Path
from abc import ABC

class Builder(Protocol):

    @staticmethod
    def build(schema_fp: Path, package_fp: Path): ...
    