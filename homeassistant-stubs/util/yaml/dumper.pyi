import yaml
from .objects import Input as Input, NodeListClass as NodeListClass
from typing import Any

def dump(_dict: dict) -> str: ...
def save_yaml(path: str, data: dict) -> None: ...
def represent_odict(dumper: Any, tag: Any, mapping: Any, flow_style: Any=...) -> yaml.MappingNode: ...