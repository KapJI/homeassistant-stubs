import voluptuous as vol
import yaml
from dataclasses import dataclass
from typing import Any

class NodeListClass(list): ...

class NodeStrClass(str):
    def __voluptuous_compile__(self, schema: vol.Schema) -> Any: ...

class NodeDictClass(dict): ...

@dataclass(slots=True, frozen=True)
class Input:
    name: str
    @classmethod
    def from_node(cls, loader: yaml.Loader, node: yaml.nodes.Node) -> Input: ...
    def __init__(self, name) -> None: ...
